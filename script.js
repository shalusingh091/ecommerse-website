let cart = [];

function addToCart(product, price) {
  cart.push({ product, price });
  displayCart();
}

function displayCart() {
  let cartItems = document.getElementById("cart-items");
  cartItems.innerHTML = "";
  let total = 0;

  cart.forEach((item) => {
    total += item.price;
    cartItems.innerHTML += `
      <div class="cart-item">
        <span>${item.product}</span>
        <span>₹${item.price}</span>
      </div>`;
  });

  document.querySelector(".total").innerText = "Total: ₹" + total;
}