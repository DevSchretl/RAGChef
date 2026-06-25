# RAGChef eval — phase1-dense-5k

2026-06-24T00:16:08 · 11 questions · k=4 · judge on

Models: chat=`google/gemma-4-e4b`, judge=`google/gemma-4-e4b`, embed=`text-embedding-nomic-embed-text-v1.5` · corpus=5000

## Summary

| metric | score |
|--------|-------|
| hit@4 | 1.000 |
| recall@4 | 1.000 |
| MRR | 0.955 |
| faithfulness | 0.978 |
| answer_relevancy | 0.840 |
| context_precision | 0.929 |
| context_recall | 1.000 |
| **hallucination_rate** | **0.022** |

## Questions

### q001 — hit — gold [2652]

**Q:** How do I make a slow-cooker potted beef roast with cream of mushroom soup and barbecue sauce?

**Reference:** Spread mashed garlic over a 3 to 4 lb beef chuck or cross-rib roast and sear it in oil in a heavy skillet on all sides. Put it in a crock-pot set on high with a can of cream of mushroom soup, 3/4 cup barbecue sauce, 1/2 cup wine or beer, and 2 tablespoons Wondra flour, and serve it over bow-tie or extra-wide noodles.

**Retrieved:** [2652] Potted Beef · [4688] Crock-Pot Sweet And Sour Beef And Vegetables · [2123] Crock-Pot Beef Tips And Gravy · [3055] Savory Pot Roast

**Answer:** To make this dish, you can follow the directions provided in **Potted Beef**.

The process involves:
1.  Spreading half of the mashed garlic on a large, flat side of the roast and searing it in hot oil in a heavy skillet or pot.
2.  Searing the remaining sides and edges of the roast.
3.  Setting the roast aside.
4.  Opening the soup can and emptying its contents into a crock-pot set on high.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.674 · context_precision 0.806 · context_recall 1.000

### q002 — hit — gold [3234]

**Q:** What goes into a broccoli and cauliflower salad with bacon and Cheddar, and how do I make the dressing?

**Reference:** In a large bowl combine broccoli florets, cauliflower florets, crumbled fried bacon, chopped onion, and chopped tomato. In another bowl mix 1 cup mayonnaise, 1/3 cup sugar, and 2 tablespoons vinegar until smooth. Just before serving, pour the dressing over the salad, toss, and add 1/2 cup shredded Cheddar.

**Retrieved:** [3234] Broccoli Salad · [3385] Broccoli Salad · [1572] Broccoli Cauliflower Salad · [1181] Broccoli Salad

**Answer:** Based on the **Broccoli Salad** recipe, you can make a salad with broccoli, cauliflower, bacon, and Cheddar cheese.

**Ingredients:**
*   1 bunch broccoli, separated into florets
*   1 head cauliflower, separated into florets
*   8 bacon strips, fried and crumbled or 1/2 c. bacon bits
*   1/3 c. chopped onion
*   1 c. chopped tomato
*   1/2 c. shredded Cheddar cheese

**To make the dressing:**
In a separate bowl, combine mayonnaise, sugar, and vinegar; mix until smooth.

**Directions Summary (from Broccoli Salad):**
1.  Combine the broccoli, cauliflower, bacon, onion, and tomatoes in a large salad bowl.
2.  Pour the prepared dressing over the salad just before serving and toss.

**Scores:** rr 1.00 · faithfulness 0.900 · answer_relevancy 0.802 · context_precision 0.917 · context_recall 1.000

### q003 — hit — gold [395]

**Q:** How do I make zucchini-slice mini pizzas under the broiler?

**Reference:** Combine 3/4 cup garden-style spaghetti sauce with minced onion, black pepper, and oregano. Arrange 1/2-inch fresh zucchini slices on a cookie sheet coated with cooking spray, top each with the sauce and a mushroom slice, sprinkle with a mix of shredded Mozzarella and grated Parmesan, and broil until hot and bubbly.

**Retrieved:** [1969] Broiled Zucchini Squash · [395] Zucchini Pizzas · [241] Zucchini In Tomato Juice(From Weight Watchers) · [3168] Mini Pizza

**Answer:** To make zucchini pizzas under the broiler, follow the directions provided in **Zucchini Pizzas**:

1.  Combine the spaghetti sauce, minced onions, black pepper, and dried oregano in a small bowl.
2.  In a separate step, combine the shredded part-skim Mozzarella cheese and grated Parmesan cheese.
3.  Place the zucchini coins on a cookie sheet that has been coated with vegetable cooking spray (keeping them approximately 1-inch apart).
4.  Top each slice with the sauce mixture, followed by a mushroom slice.
5.  Sprinkle the toppings with the combined cheese mixture.
6.  Bake under the broiler until the pizza is hot and bubbly.

**Scores:** rr 0.50 · faithfulness 1.000 · answer_relevancy 0.859 · context_precision 0.500 · context_recall 1.000

### q004 — hit — gold [593]

**Q:** How do I make an Orange Julius drink in the blender with fresh oranges and honey?

**Reference:** Put a couple of oranges and 2 tablespoons honey in a blender, add crushed ice until it reaches the thickness you want, then add about 1 cup of milk to fill the blender and blend.

**Retrieved:** [593] Orange Julius · [4245] Orange Julius · [2711] Orange Julius · [2295] Orange Julius

**Answer:** To make an Orange Julius drink using fresh oranges and honey, follow the instructions provided in the **Orange Julius** recipe:

1.  Put a couple of oranges and 2 Tbsp. of honey into the blender.
2.  Add crushed ice until you reach your desired thickness.
3.  Pour enough milk into the blender to fill it, which is approximately 1 cup.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.877 · context_precision 1.000 · context_recall 1.000

### q005 — hit — gold [771]

**Q:** How do I make oven Swiss steak using an oven roasting bag?

**Reference:** Shake 1 tablespoon flour inside an oven cooking bag, then add pieces of round or sirloin steak, a 16 oz can of Italian seasoned tomatoes, a dry envelope of Lipton onion soup mix, 1/4 cup water, and salt and pepper. Squeeze to mix, tie the bag, place it in a 9 x 13-inch pan, cut six 1/2-inch vent slits, and bake at 325 degrees for about 2 hours.

**Retrieved:** [771] Oven Swiss Steak · [2407] Oven Swiss Steak · [4207] Swiss Steak · [3843] Swiss Steak

**Answer:** To make oven Swiss steak using an oven cooking bag, follow these steps from **Oven Swiss Steak**:

1. Shake 1 tablespoon flour in the oven cooking bag.
2. Add all ingredients to the bag and squeeze to mix.
3. Tie the bag and place it in a 9 x 13-inch pan.
4. Slit the bag with six (1/2") cuts to vent.
5. Bake at 325° for approximately 2 hours.
6. When ready to serve, slit open the bag and put it back in the pan.

**Scores:** rr 1.00 · faithfulness 0.857 · answer_relevancy 0.904 · context_precision 1.000 · context_recall 1.000

### q006 — hit — gold [4774]

**Q:** How do I brine and jar Grandma's dill pickles?

**Reference:** Wash firm cucumbers and pack them into jars. To each quart add 1/2 teaspoon mustard seed, 1/2 teaspoon celery seed, 1 bay leaf, 1/2 teaspoon pickling spice, and a large piece of dill. Bring 5 quarts water, 1 cup salt, and 2 cups vinegar to a boil, fill the packed jars with the hot brine, and seal at once; they can be used after standing 1 week.

**Retrieved:** [4774] Grandma'S Best Dill Pickles · [480] Ma'S Dill Pickles · [2942] Dill Pickles · [3049] Pickles

**Answer:** To brine and jar Grandma's dill pickles, follow these steps according to **Grandma'S Best Dill Pickles**:

1.  Wash cucumbers and pack them into jars.
2.  For each quart of jars, add 1/2 teaspoon mustard seed, 1/2 teaspoon celery seed, 1 bay leaf, 1/2 teaspoon pickling spice, and 1 large piece of dill.
3.  Bring the water, salt, and vinegar to a boiling point; then fill the cucumber-filled jars with this syrup immediately.
4.  Seal the jars at once.

The pickles can be used after one week's standing.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.834 · context_precision 1.000 · context_recall 1.000

### q007 — hit — gold [475]

**Q:** How do I make Spanish hamburger with tomato soup on the stovetop?

**Reference:** Fry the hamburger until half done, then add finely chopped onion, green pepper, and celery and let it simmer 1/2 hour. Season with salt and pepper, stir in a 20 oz can of tomato soup, and simmer 2 hours, keeping the steam in for best results.

**Retrieved:** [475] Spanish Hamburger #1 · [3522] Hamburger Soup · [1846] Hamburger Hot Dish · [551] Easy Hot Dish

**Answer:** To make Spanish Hamburger with tomato soup, follow the directions provided in **Spanish Hamburger #1**:

1.  Fry the hamburger until it is half done.
2.  Cut the onion, green pepper, and celery into fine pieces and add them to the pot.
3.  Let the mixture simmer for 1/2 hour.
4.  Add salt and pepper, then pour in the tomato soup. Simmer the dish for 2 hours.
5.  Keep steam in for the best results.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.927 · context_precision 1.000 · context_recall 1.000

### q008 — hit — gold [4156]

**Q:** How do I marinate and bake Chinese five-spice chicken wings?

**Reference:** Combine 2/3 cup soy sauce, 1/2 cup honey, 2 tablespoons vegetable oil, 2 minced garlic cloves, and 2 teaspoons Chinese Five Spice powder, and pour it over 2 1/2 lb chicken wings. Marinate 4 hours, then place the wings on a broiler rack and bake at 375 degrees for 45 minutes, turning and basting every 15 minutes.

**Retrieved:** [4156] Chinese Chicken Wings · [4241] Chinese Chicken Wings · [2660] Chicken Wings · [2616] Chicken Wing Drumsticks

**Answer:** To marinate and bake Chinese Five Spice Chicken Wings, follow these steps using the instructions from the **Chinese Chicken Wings** recipe:

**Marinating:**
1. Combine the soy sauce, honey, oil, garlic, and Chinese Five Spice powder.
2. Pour this mixture over the chicken wings.
3. Marinate for 4 hours.

**Baking:**
1. Remove the wings and place them on a broiler rack.
2. Bake at 375° for 45 minutes, making sure to turn and baste every 15 minutes.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.887 · context_precision 1.000 · context_recall 1.000

### q009 — hit — gold [704]

**Q:** How do I make a strawberry Jell-O salad with bananas, pecans, and Cool Whip?

**Reference:** Dissolve 2 large packages of strawberry Jell-O in 2 cups boiling water, then stir in the rest of the water (4 cups hot water total). Let it begin to thicken, then add a pint of strawberries, 3 diced bananas, and 1 cup chopped pecans. Let it stand until firm, spread Cool Whip on top, and refrigerate.

**Retrieved:** [704] Strawberry Salad · [941] Strawberry Salad · [526] Strawberry Salad · [2790] Jello Salad

**Answer:** To make a strawberry salad with bananas, pecans, and Cool Whip, you can follow the directions in **Strawberry Salad** (Recipe 1).

The steps are:
1. Mix the Jell-O with 2 cups of boiling water, then add the rest of the water. Let it set until it begins to thicken.
2. Add the fruit and nuts.
3. Allow it to stand until firm.
4. Spread Cool Whip on top.
5. Refrigerate.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.826 · context_precision 1.000 · context_recall 1.000

### q010 — hit — gold [3552]

**Q:** How do I make a filled beef roll stuffed with rice and Swiss cheese?

**Reference:** Combine a beaten egg, 1/4 cup milk, 1/2 cup finely crushed saltine crumbs, 1/4 cup chopped onion, 1/2 teaspoon salt, and a dash of pepper, then mix in 1 lb ground beef. Pat it into a 10 x 8-inch rectangle on waxed paper. Mix 1 cup cooked rice, shredded process Swiss cheese, and chopped green pepper and pat it onto the meat leaving a 1-inch margin. Roll jelly-roll fashion from the narrow side, seal the seam and ends, and bake seam side down at 350 degrees for 35 minutes; let stand 5 minutes before serving.

**Retrieved:** [3552] Filled Beef Roll · [3804] Ham And Swiss Rolls · [4207] Swiss Steak · [3961] Sausage And Wild Rice

**Answer:** To make a filled beef roll stuffed with rice and Swiss cheese, follow the directions in **Filled Beef Roll**:

1.  Combine the cooked rice, shredded Swiss cheese, and chopped green pepper.
2.  Pat this mixture onto the meat, making sure to leave a 1-inch margin around the edge.
3.  Roll the beef roll up like a jelly roll, starting with the narrow side.
4.  Seal both the ends and the side seam.
5.  Place the roll in an 11 x 7 x 1 1/2-inch baking pan, seam side down.
6.  Bake at 350° for 35 minutes, and let it stand for 5 minutes before serving.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.792 · context_precision 1.000 · context_recall 1.000

### q011 — hit — gold [3425]

**Q:** How do I make chicken Creole starting with a roux, served over rice?

**Reference:** Heat 1/4 cup vegetable oil in a heavy skillet, stir in 1/4 cup flour, and stir constantly until it turns the color of a copper penny, about 5 minutes. Reduce heat, add chopped green pepper and onion, and cook until tender. Add 2 cups cooked chicken, a 28 oz can of stewed tomatoes, Worcestershire sauce, minced garlic, soy sauce, sugar, salt, pepper, and hot sauce; cover and simmer about 20 minutes, then serve over hot cooked rice.

**Retrieved:** [3425] Chicken Creole · [3956] Cajun Chicken Creole · [302] Chicken Over Rice · [3303] Chicken And Wild Rice

**Answer:** To make Chicken Creole starting with a roux and serving it over rice, follow the directions in **Chicken Creole**:

1.  Heat vegetable oil in a heavy skillet until hot, then stir in 1/4 cup flour. Stir constantly until the mixture is about the color of a copper penny (this takes about 5 minutes).
2.  Reduce the heat and add the pepper and onion; cook until tender (about 10 minutes), stirring constantly.
3.  Add the chicken, tomatoes, Worcestershire sauce, garlic, soy sauce, sugar, pepper, salt, and hot sauce.
4.  Cover and simmer for about 20 minutes.
5.  Serve the dish over rice.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.851 · context_precision 1.000 · context_recall 1.000

