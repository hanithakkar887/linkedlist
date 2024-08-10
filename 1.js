const products = [
    { name: "Laptop", category: "Electronics", price: 1200, quantity: 10, available: true },
    { name: "Chair", category: "Furniture", price: 100, quantity: 20, available: true },
    { name: "Shirt", category: "Clothing", price: 30, quantity: 50, available: false },
    { name: "Book", category: "Books", price: 20, quantity: 100, available: true },
  ];
  
  // 1. Filter Products by Availability
  const filteredProducts = products.filter(product => product.available);
  console.log("Filtered Products:", filteredProducts);
  
  // 2. Sort Products by Price
  const sortedProducts = [...products].sort((a, b) => a.price - b.price);
  console.log("Sorted Products by Price:", sortedProducts);
  
  // 3. Calculate Total Value for Each Product
  const productsWithTotalValue = products.map(product => ({
    ...product,
    totalValue: product.price * product.quantity,
  }));
  console.log("Products with Total Value:", productsWithTotalValue);
  