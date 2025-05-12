

### Scenario: Processing a Product's Details

Imagine we have a product object with nested properties, and we want to process its details for display:

1. We need to check the product's **availability**.
2. Retrieve the **discounted price** if available.
3. Format the **price**.
4. Ensure the **category** exists and is valid.    
5. Fallback to default values if any of the above are missing or invalid.


Here’s how we could structure this problem with the **Maybe Monad**.

### Example: Processing Product Details with Multiple Transformations


### Product Object Example

```ts
const product = {
  price: 100,
  discount: { percentage: 20 },
  category: "electronics",
  availability: "in-stock",
};
```

### Complex Chain Using Maybe Monad

```ts
function getDiscountedPrice(product: any): string {
  return maybe(product)
    .filter(p => p.availability === "in-stock")
    .flatMap(p => maybe(p.discount?.percentage)
      .map(discountPercent => ({
        price: p.price,
        discountPercent
      }))
    )
    .map(({ price, discountPercent }) => price * (1 - discountPercent / 100))
    .map(discounted => discounted.toFixed(2))
    .getOrElse("Price unavailable");
}
```



```ts
function getDiscountedPrice(product: any): string {
  const inStock = maybe(product).filter(p => p.availability === "in-stock");

  const discountInfo = inStock.flatMap(p =>
    maybe(p.discount?.percentage).map(discountPercent => ({
      price: p.price,
      discountPercent
    }))
  );

  const discountedPrice = discountInfo.map(({ price, discountPercent }) => {
    return price * (1 - discountPercent / 100);
  });

  const formattedPrice = discountedPrice.map(discounted => discounted.toFixed(2));

  return formattedPrice.getOrElse("Price unavailable");
}

```

### Optional Chaining (Nullish Coalescing) Alternative 

If we tried using **optional chaining** and **nullish coalescing** for the same scenario, it would quickly become less readable:

```ts
const discountedPrice = (product?.availability === "in-stock" &&
  product?.discount?.percentage) ? 
  (product.price * (1 - product.discount.percentage / 100)).toFixed(2) : 
  "Price unavailable";

console.log(discountedPrice);  // "80.00"
```


```ts
const isInStock = product?.availability === "in-stock";
const discountPercent = product?.discount?.percentage;
const price = product?.price;

let discountedPrice: string;

if (isInStock) {
  if (discountPercent) {
    const discounted = price * (1 - discountPercent / 100);
    discountedPrice = discounted.toFixed(2);
  } else {
    discountedPrice = "Price unavailable";  // No discount percentage
  }
} else {
  discountedPrice = "Price unavailable";  // Product not in stock
}

console.log(discountedPrice);  // e.g. "80.00"

```


```ts
const isInStock = product?.availability === "in-stock";
const discountPercent = product?.discount?.percentage;
const price = product?.price;

let discountedPrice: string;

if (isInStock && discountPercent) {
  const discounted = price * (1 - discountPercent / 100);
  discountedPrice = discounted.toFixed(2);
} else {
  discountedPrice = "Price unavailable";
}

console.log(discountedPrice);  // e.g. "80.00"
```



The **Maybe Monad** excels when you need to safely handle more complex logic involving multiple transformations, conditions, and fallbacks. In cases where **optional chaining** might become verbose or difficult to manage, **Maybe** provides a clean, composable, and readable solution.






```ts
const product = {
  price: 150,
  availability: "in-stock",
  discount: { percentage: 20 },
  isVIP: true,
  promoCode: "PROMO10",
  flashSale: true,
  origin: { self: true },
};

console.log(discountedPrice);  // Example output: "55.00"

```



```ts
const priceThreshold = 100;  // Define the price threshold for regular discount
const defaultDiscount = 5;   // Default discount percentage if price is below threshold
const vipDiscount = 15;      // VIP discount percentage
const promoDiscount = 10;    // Promo code discount percentage
const flashSaleDiscount = 20; // Flash sale discount percentage
const specialDiscount = 10;  // Special discount for self-origin products

const discountedPrice = maybe(product)
  .filter(p => p.availability === "in-stock")  // Ensure product is in stock
  .flatMap(p => maybe(p.price))  // Get the price, if available
  .flatMap(price => {
    // Apply price-based discount logic
    let discountPercent = price > priceThreshold
      ? maybe(p.discount?.percentage).getOrElse(0)  // Use product discount if available
      : defaultDiscount;  // Use default discount for lower prices
    
    // Apply VIP discount if the product is VIP
    discountPercent = maybe(p.isVIP).filter(isVIP => isVIP === true)
      .map(() => discountPercent + vipDiscount)
      .getOrElse(discountPercent);  // Apply VIP discount if VIP flag is true

    // Apply promo code discount if available
    discountPercent = maybe(p.promoCode).filter(code => code === "PROMO10")
      .map(() => discountPercent + promoDiscount)
      .getOrElse(discountPercent);  // Apply promo discount if valid

    // Apply flash sale discount if applicable
    discountPercent = maybe(p.flashSale).filter(sale => sale === true)
      .map(() => discountPercent + flashSaleDiscount)
      .getOrElse(discountPercent);  // Apply flash sale discount if true

    // Apply additional discount for self-origin products
    discountPercent = maybe(p.origin?.self).filter(isSelf => isSelf === true)
      .map(() => discountPercent + specialDiscount)
      .getOrElse(discountPercent);  // Apply special self-origin discount

    return price * (1 - discountPercent / 100);  // Calculate final discounted price
  })
  .map(discounted => discounted.toFixed(2))  // Format the final discounted price
  .getOrElse("Price unavailable");  // Return fallback if any step fails

console.log(discountedPrice);  // Example output: "75.00" (after applying all discounts)

```



```ts
// Constants for discount types
const priceThreshold = 100;
const defaultDiscount = 5;
const vipDiscount = 15;
const promoDiscount = 10;
const flashSaleDiscount = 20;
const specialDiscount = 10;

// Helper functions for discounts (pure functions)
const applyPriceBasedDiscount = (price: number): number => 
  price > priceThreshold ? 0 : defaultDiscount;

const applyVIPDiscount = (isVIP: boolean, discount: number): number =>
  isVIP ? discount + vipDiscount : discount;

const applyPromoDiscount = (promoCode: string | undefined, discount: number): number =>
  promoCode === "PROMO10" ? discount + promoDiscount : discount;

const applyFlashSaleDiscount = (flashSale: boolean, discount: number): number =>
  flashSale ? discount + flashSaleDiscount : discount;

const applySelfOriginDiscount = (isSelfOrigin: boolean | undefined, discount: number): number =>
  isSelfOrigin ? discount + specialDiscount : discount;

// Composing all the discount functions into one
const applyAllDiscounts = (product: any, baseDiscount: number): number => {
  const price = product.price;

  // Apply all discounts in a functional pipeline manner
  return [
    applyPriceBasedDiscount(price),
    applyVIPDiscount(product.isVIP, baseDiscount),
    applyPromoDiscount(product.promoCode, baseDiscount),
    applyFlashSaleDiscount(product.flashSale, baseDiscount),
    applySelfOriginDiscount(product.origin?.self, baseDiscount)
  ].reduce((discount, applyDiscount) => applyDiscount(discount), baseDiscount);
}

// Main function to calculate the discounted price
const calculateDiscountedPrice = (product: any): string => 
  maybe(product)
    .filter(p => p.availability === "in-stock") // Ensure product is in stock
    .flatMap(p => maybe(p.price))  // Get price safely
    .map(price => {
      // Start with base discount (e.g., default value) and apply all discount functions
      let baseDiscount = applyPriceBasedDiscount(price);  // Start with base discount (for price)

      const finalDiscount = applyAllDiscounts(p, baseDiscount);  // Apply all the discounts
      return price * (1 - finalDiscount / 100);  // Final price after all discounts
    })
    .map(discountedPrice => discountedPrice.toFixed(2))  // Format the final discounted price
    .getOrElse("Price unavailable");  // Return fallback if any step fails

// Example product object
const product = {
  price: 150,
  availability: "in-stock",
  isVIP: true,
  promoCode: "PROMO10",
  flashSale: true,
  origin: { self: true },
};

console.log(calculateDiscountedPrice(product));  // Example output: "55.00" (after applying all discounts)

```


```ts
function getDiscountedPriceImperative(product: any): string {
  // Step 1: Check if the product is in stock
  if (!product || product.availability !== "in-stock") {
    return "Price unavailable";
  }

  // Step 2: Check for price
  const price = product.price;
  if (price === undefined || price === null) {
    return "Price unavailable";
  }

  // Step 3: Apply the base discount based on price threshold
  let discountPercent = price > 100
    ? product.discount?.percentage || 0  // Use product discount if available
    : 5;  // Default discount for lower-priced items

  // Step 4: Apply VIP discount if available
  if (product.isVIP) {
    discountPercent += 15;  // Apply VIP discount
  }

  // Step 5: Apply promo code discount if available
  if (product.promoCode === "PROMO10") {
    discountPercent += 10;  // Apply promo discount
  }

  // Step 6: Apply flash sale discount if available
  if (product.flashSale === true) {
    discountPercent += 20;  // Apply flash sale discount
  }

  // Step 7: Apply self-origin discount if applicable
  if (product.origin?.self === true) {
    discountPercent += 10;  // Apply self-origin discount
  }

  // Step 8: Calculate the final discounted price
  const discountedPrice = price * (1 - discountPercent / 100);

  // Step 9: Format the final price
  return discountedPrice.toFixed(2);
}



```



```ts
function getDiscountedPriceOptionalChaining(product: any): string {
  // Check if the product is in stock and has a price
  const price = product?.availability === "in-stock" ? product?.price : undefined;

  if (!price) return "Price unavailable";

  // Apply base discount based on price threshold
  let discountPercent = price > 100
    ? product?.discount?.percentage || 0
    : 5;  // Default discount for lower-priced items

  // Apply VIP discount if available
  discountPercent += product?.isVIP ? 15 : 0;

  // Apply promo code discount if available
  discountPercent += product?.promoCode === "PROMO10" ? 10 : 0;

  // Apply flash sale discount if available
  discountPercent += product?.flashSale ? 20 : 0;

  // Apply self-origin discount if applicable
  discountPercent += product?.origin?.self ? 10 : 0;

  // Calculate the final discounted price
  const discountedPrice = price * (1 - discountPercent / 100);

  // Return the formatted discounted price
  return discountedPrice.toFixed(2);
}

```



