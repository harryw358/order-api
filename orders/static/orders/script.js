const BASE_URL = 'http://127.0.0.1:8000/api';

// --- API Calls ---

async function loadAnalytics() {
    try {
        const response = await fetch(`${BASE_URL}/orders/analytics/summary/`);
        const data = await response.json();
        
        document.getElementById('page-title').innerText = "Analytics Summary";
        document.getElementById('total-orders-count').innerText = data.metrics.total_orders_tracked;
        document.getElementById('items-in-stock').innerText = data.metrics.physical_items_in_stockroom;
        
        const statusList = document.getElementById('status-list');
        statusList.innerHTML = '';
        for (const [status, count] of Object.entries(data.status_breakdown)) {
            statusList.innerHTML += `<div class="status-chip">${status}: ${count}</div>`;
        }
    } catch (err) {
        console.error("Failed to load analytics", err);
    }
}

async function loadOrders() {
    const grid = document.getElementById('main-grid');
    document.getElementById('page-title').innerText = "All Orders";
    
    try {
        const response = await fetch(`${BASE_URL}/orders/`);
        const orders = await response.json();
        
        grid.innerHTML = `
            <div class="block full-width">
                <table>
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Customer</th>
                            <th>Status</th>
                            <th>Items</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${orders.map(o => `
                            <tr>
                                <td>${o.id}</td>
                                <td>${o.customer_id}</td>
                                <td>${o.order_status}</td>
                                <td>${o.total_items}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    } catch (err) {
        grid.innerHTML = `<p>Error loading orders.</p>`;
    }
}

async function searchCustomer() {
    const cid = document.getElementById('customerSearch').value;
    if (!cid) return;

    try {
        const response = await fetch(`${BASE_URL}/customers/${cid}/orders/`);
        if (response.status === 404) {
            alert("No orders found for this customer.");
            return;
        }
        const orders = await response.json();
        // Reuse table logic to show results...
        loadOrdersListInUI(orders, `Orders for ${cid}`);
    } catch (err) {
        console.error(err);
    }
}

// Initial Load
window.onload = loadAnalytics;