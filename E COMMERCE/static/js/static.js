document.addEventListener("DOMContentLoaded", function() {
    const categoryLinks = document.querySelectorAll(".category-link");
    
    categoryLinks.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            let category = this.getAttribute("data-category");

            fetch(`/api/products/?category=${category}`)
                .then(response => response.json())
                .then(data => {
                    const productGrid = document.getElementById("product-grid");
                    productGrid.innerHTML = "";

                    data.forEach(product => {
                        let productHTML = `
                            <div class="bg-white p-4 rounded-lg shadow-md product-item">
                                <img src="${product.image}" alt="${product.name}" class="w-full h-40 object-cover rounded-md">
                                <h3 class="text-lg font-semibold mt-2 product-name">${product.name}</h3>
                                <p class="text-gray-600">${product.category}</p>
                                <p class="text-green-600 font-bold">Rp ${product.price}</p>
                            </div>
                        `;
                        productGrid.innerHTML += productHTML;
                    });
                });
        });
    });
});
