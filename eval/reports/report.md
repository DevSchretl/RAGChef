# RAGChef eval — phase1-dense-hard

2026-07-02T18:57:52 · 24 questions · k=4 · judge on

Models: chat=`google/gemma-4-e4b`, judge=`google/gemma-4-e4b`, embed=`text-embedding-nomic-embed-text-v1.5` · corpus=50000

## Summary

| metric | score |
|--------|-------|
| hit@4 | 0.583 |
| recall@4 | 0.481 |
| MRR | 0.486 |
| faithfulness | 0.792 |
| answer_relevancy | 0.853 |
| context_precision | 0.601 |
| context_recall | 0.708 |
| **hallucination_rate** | **0.208** |

## Questions

### q001 — hit — gold [6173]

**Q:** I want a quick white sauce without making a roux first — which recipe uses Gold Medal Wondra instant flour?

**Reference:** Mix 1 cup milk, 2 tablespoons Gold Medal Wondra flour, 1/4 teaspoon salt, 1/8 teaspoon white pepper, and 2 tablespoons margarine in a 1-quart saucepan. Heat to a boil over medium heat, stirring constantly, then boil and stir for 1 minute; it makes 1 cup of sauce.

**Retrieved:** [6173] One-Step White Sauce · [12645] Quick White Sauce · [15662] Rolls With Gold Medal Flour · [31087] Instant Delite

**Answer:** The recipe that uses Gold Medal wondra flour and is a white sauce is **One-Step White Sauce**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.871 · context_precision 1.000 · context_recall 1.000

### q002 — hit — gold [20163]

**Q:** Which popover recipe is flavored with Cheddar and dill and is made with Wondra flour?

**Reference:** Heat the oven to 450 degrees and grease custard or muffin cups. Beat 2 eggs, then stir in 1 cup Gold Medal Wondra flour, 1 cup milk, 1/4 cup shredded Cheddar, 1/2 teaspoon salt, and 1/2 teaspoon dried dill just until smooth. Fill the cups, bake 25 minutes, then reduce to 325 degrees and bake 10 to 15 minutes more until deep golden brown.

**Retrieved:** [20163] Cheddar-Dill Popovers · [23583] Popovers · [7684] Popovers(Portuguese) · [30475] Cheddar Cheese Popovers

**Answer:** The recipe that is flavored with Cheddar, dill, and uses Wondra flour is **Cheddar-Dill Popovers**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.760 · context_precision 1.000 · context_recall 1.000

### q003 — hit — gold [37876]

**Q:** How do I make a ham glaze using Dr. Pepper?

**Reference:** Mix 1 cup Dr. Pepper with 1/2 cup brown sugar. Place the ham in a baking pan and baste it frequently with the sauce as it bakes; you can still decorate with cloves or cherries.

**Retrieved:** [37876] Dr.  Pepper Glaze · [44544] Glaze For Ham · [47128] Honey Orange Glaze Ham · [21622] Beer Glaze For Ham

**Answer:** To make a ham glaze using Dr. Pepper, follow the instructions in **Dr. Pepper Glaze**:

1. Mix 1 c. Dr. Pepper and 1/2 c. brown sugar.
2. Place ham in a baking pan and baste frequently with the sauce.
3. You can use cloves or cherries for decoration.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.919 · context_precision 1.000 · context_recall 1.000

### q004 — hit — gold [48419]

**Q:** Which strawberry pie is thickened with a strawberry Danish Junket dessert mix instead of cornstarch or gelatin?

**Reference:** Mix 1 quart strawberries with 1 cup powdered sugar and let stand. Drain the juice and add water to make 2 cups, cook briefly, then stir in a box of strawberry Danish Junket mix. Cool, fold in the berries, pour into a baked pie shell, and top with whipped cream.

**Retrieved:** [48419] Strawberry Pie · [12834] Strawberry Pie · [7767] Strawberry Pie · [18558] Strawberry Pie

**Answer:** The recipe that thickens the pie with a strawberry Danish Junket mix instead of cornstarch or gelatin is the first **Strawberry Pie**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.927 · context_precision 1.000 · context_recall 1.000

### q005 — miss — gold [38276]

**Q:** Which biscuit recipe calls specifically for Clabber Girl baking powder?

**Reference:** Combine 1 1/2 cups flour, a dash of salt, 2 tablespoons Clabber Girl baking powder, and 3 tablespoons oil, then add buttermilk until the dough is moist and sticky. Turn it out onto a floured surface, press it out by hand, and cut the biscuits.

**Retrieved:** [33834] Biscuits · [12806] Old-Time Biscuit Pudding · [33938] Baking Powder Biscuits · [42024] Flaky Baking Powder Biscuits

**Answer:** The provided recipes do not specify or call for Clabber Girl baking powder.

**Scores:** rr 0.00 · faithfulness 0.000 · answer_relevancy 0.863 · context_precision 0.000 · context_recall 0.000

### q006 — miss — gold [2400]

**Q:** Which onion soup uses three kinds of onion and a little Kitchen Bouquet?

**Reference:** Saute 1 red, 2 white, and 3 yellow onions with garlic in a stick of margarine until tender. Add sugar, thyme, black pepper, caraway seed, a bay leaf, Worcestershire sauce, 1/2 teaspoon Kitchen Bouquet, and 2 quarts beef stock, and cook about 1 hour in a crock-pot on high or simmer on the stove.

**Retrieved:** [41058] "Venus De Milo" Style Soup · [39657] Joyce Yawn'S French Onion Soup · [25441] French Onion Soup(Serves 4) · [17066] Sarah Matt'S Onion Soup

**Answer:** Based on the provided recipes, there is no mention of an onion soup using three kinds of onion or Kitchen Bouquet.

**Scores:** rr 0.00 · faithfulness 0.000 · answer_relevancy 0.854 · context_precision 0.250 · context_recall 0.000

### q007 — hit — gold [8640]

**Q:** Which blueberry pie filling is thickened with Minute tapioca?

**Reference:** Combine 2 tablespoons Minute tapioca with brown sugar, lemon juice or vinegar, cold water, sugar, salt, a quart of blueberries, and butter, then cook and pour the filling into a baked pie shell.

**Retrieved:** [8640] Blueberry Pie(You Won'T Feel Blue After Eating This Pie.) · [28185] Fresh Blueberry Pie · [39479] Blueberry Pie · [29466] Blueberry Pie

**Answer:** The blueberry pie filling thickened with Minute tapioca is found in **Blueberry Pie(You Won'T Feel Blue After Eating This Pie.)**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.952 · context_precision 1.000 · context_recall 1.000

### q008 — hit — gold [28646]

**Q:** Which pumpkin tea loaf is spiced with cardamom along with cloves and cinnamon?

**Reference:** Beat shortening and sugar, then beat in 4 eggs, a 1-lb can of pumpkin, and water. Combine all-purpose and whole wheat flours with soda, salt, baking powder, ground cardamom, cloves, and cinnamon; stir into the pumpkin mixture, fold in raisins and chopped pecans, and bake in greased loaf pans.

**Retrieved:** [49694] Pumpkin-N-Spice Tea Bread · [19835] Pumpkin Tea Bread · [28646] Pumpkin-Pecan Tea Loaf · [41319] Halloween Bread(A Spook Brings This To Us)

**Answer:** The **Pumpkin-Pecan Tea Loaf** is spiced with cardamom, ground cloves, and ground cinnamon.

**Scores:** rr 0.33 · faithfulness 1.000 · answer_relevancy 0.842 · context_precision 0.333 · context_recall 1.000

### q009 — miss — gold [214]

**Q:** Which party punch gets its color and flavor from grenadine syrup and ginger ale?

**Reference:** Combine thawed frozen lemonade and orange juice concentrates, 6 cups water, and grenadine syrup in a punch bowl. Just before serving, add ice and stir in a quart of chilled ginger ale, garnishing each cup with a thin lemon slice and a maraschino cherry.

**Retrieved:** [35775] Party Punch · [42892] Pink Punch · [609] Pretty Party Punch · [37683] Party Punch

**Answer:** Based on the recipes provided, none of the party punches listed use grenadine syrup.

**Scores:** rr 0.00 · faithfulness 1.000 · answer_relevancy 0.786 · context_precision 0.250 · context_recall 0.000

### q010 — hit — gold [744]

**Q:** Which spice cake is seasoned with both cardamom and cilantro, with apple, apricots, and raisins?

**Reference:** Beat 4 eggs with 1 3/4 cups brown sugar and salt, then add allspice, cinnamon, cardamom, cilantro, ginger, and cloves. Cut walnuts, raisins, dried apricots, and an apple into pieces, toss them with the wheat flour, fold into the batter, and bake at 350 degrees.

**Retrieved:** [744] "Spicy" Cake · [43931] Sun-Maid Raisin Nut Cake(Our Family Christmas Cake Since 1936) · [16416] Applesauce Raisin Spice Cake · [8942] Spice Cake

**Answer:** The recipe that is seasoned with both cardamom and cilantro, and includes apple, apricots, and raisins, is **"Spicy" Cake**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.901 · context_precision 1.000 · context_recall 1.000

### q011 — hit — gold [47608]

**Q:** Which root beer float is decorated like eyeballs with ice cream, candies, and gummy worms?

**Reference:** Scoop vanilla ice cream into eyeball-sized balls and press a chocolate-coated candy into each as a pupil, then freeze. Fill serving glasses with chilled root beer to 2 inches from the top, add a small scoop of ice cream, drop in gummy worms and shoestring licorice as 'veins,' and top with the ice cream eyeballs.

**Retrieved:** [47608] Eye-Scream Float · [49949] Root Sherbet Float · [35542] Ice Cream Float · [46604] Bubble Brew

**Answer:** The root beer float decorated like eyeballs with ice cream, candies, and gummy worms is the **Eye-Scream Float**.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.872 · context_precision 1.000 · context_recall 1.000

### q012 — miss — gold [2652]

**Q:** Which slow-cooker beef roast thickens its gravy with Gold Medal Wondra flour and is served over bow-tie noodles?

**Reference:** Spread mashed garlic over a 3 to 4 lb beef chuck or cross-rib roast and sear it in oil. Put it in a crock-pot on high with a can of cream of mushroom soup, 3/4 cup barbecue sauce, 1/2 cup wine or beer, and 2 tablespoons Gold Medal Wondra flour, and serve it over bow-tie or extra-wide noodles.

**Retrieved:** [48536] Beef Roast · [46840] Italian Beef Au Jus · [45594] Slow Cooker Beef · [19740] Beef Roast Cooked In Crock-Pot

**Answer:** Based on the recipes provided, there is no information regarding a slow-cooker beef roast that thickens its gravy with Gold Medal Wondra flour or specifies serving it over bow-tie noodles.

**Scores:** rr 0.00 · faithfulness 0.000 · answer_relevancy 0.806 · context_precision 0.250 · context_recall 0.714

### q013 — miss — gold [2888, 8775]

**Q:** Among the many strawberry pies, which is the no-bake kind made with cream cheese and sweetened condensed milk (Eagle Brand), not a cooked cornstarch or gelatin glaze?

**Reference:** Beat an 8-oz package of cream cheese with a can of sweetened condensed milk (Eagle Brand), then mix in lemon juice and fold in strawberries. Pour into a graham cracker or baked pie shell and chill or freeze — there is no cooked cornstarch or gelatin glaze.

**Retrieved:** [38297] No Bake Strawberry Pie · [41339] No Bake Cheese Cake · [6659] Strawberry Cream Cheese Pie · [20079] No Bake Cherry Cheese Pie

**Answer:** Based on the recipes provided, there is no recipe for a no-bake strawberry pie that uses both cream cheese and sweetened condensed milk (specifically mentioning Eagle Brand) while avoiding cornstarch or gelatin.

**Scores:** rr 0.00 · faithfulness 0.000 · answer_relevancy 0.911 · context_precision 0.250 · context_recall 0.500

### q014 — hit — gold [8042, 9379, 19984, 22976, 37768]

**Q:** Which carrot cake includes both crushed pineapple and coconut in the batter?

**Reference:** Mix flour, sugar, coconut, baking soda, cinnamon, and salt, then add beaten eggs, oil, grated carrots, chopped walnuts, a can of crushed pineapple, and vanilla. Pour into a greased and floured pan and bake at 325 to 350 degrees for 45 to 50 minutes.

**Retrieved:** [24251] "Lite" Carrot Cake · [3839] Famous Carrot Cake · [22976] Carrot Cake · [40462] Carrot Cake

**Answer:** The "Carrot Cake" recipe includes both crushed pineapple and coconut in the batter.

**Scores:** rr 0.33 · faithfulness 1.000 · answer_relevancy 0.859 · context_precision 0.333 · context_recall 0.500

### q015 — hit — gold [8208]

**Q:** Which broccoli salad is dressed with sour cream, mayonnaise, and Ranch dressing mix (and includes cauliflower and peas) instead of the usual sugar-vinegar dressing?

**Reference:** Mix broccoli and cauliflower florets, thawed frozen peas, sliced celery, and chopped green onions. Stir together an 8-oz carton of sour cream, 1 cup mayonnaise, and 2 packages of Ranch dressing mix, pour over the vegetables, and refrigerate several hours or overnight.

**Retrieved:** [41391] Broccoli Cauliflower Salad · [8208] Broccoli Salad · [46353] Broccoli-Cauliflower Salad · [36099] Broccoli Salad

**Answer:** The salad that uses sour cream, mayonnaise, and Ranch dressing mix (and includes cauliflower and peas) instead of a sugar-vinegar dressing is the **Broccoli Salad** ([Recipe 2]).

**Scores:** rr 0.50 · faithfulness 1.000 · answer_relevancy 0.849 · context_precision 0.500 · context_recall 1.000

### q016 — miss — gold [20932, 34944, 44209]

**Q:** Which banana bread has raisins folded into the batter?

**Reference:** Mash very ripe bananas and mix with the wet ingredients, then fold in the dry ingredients along with raisins, taking care not to overmix. Pour into a greased loaf pan and bake at 350 degrees.

**Retrieved:** [29656] Banana Raisin Bread · [4771] Banana-Nut Raisin Bread · [6568] Banana Nut Bread With Raisins · [3119] Banana Nut Bread(Diabetic)

**Answer:** Three of the recipes include raisins folded into the batter:

*   **Banana Raisin Bread:** The directions instruct you to "Add raisins" before pouring over the dry ingredients.
*   **Banana-Nut Raisin Bread:** In step 5, you are instructed to "Stir in chopped pecans and raisins."
*   **Banana Nut Bread With Raisins:** The instructions state that after mixing everything else, you should "Add nuts and raisins last."

**Scores:** rr 0.00 · faithfulness 1.000 · answer_relevancy 0.816 · context_precision 1.000 · context_recall 1.000

### q017 — miss — gold [12778]

**Q:** Which chocolate pie has dairy sour cream stirred into the cooked filling?

**Reference:** Cook a mixture of granulated and brown sugar, salt, cornstarch, evaporated milk, and beaten egg yolks until thick, then stir in 1 cup dairy sour cream, butter, vanilla, and cocoa. Pour into a baked pie shell and top with whipped topping.

**Retrieved:** [39324] Sour Cream Pie · [31260] Favorite Chocolate Cake With Sour Milk · [8261] The Best Chocolate Pie · [1230] Chocolate Pudding Or Pie Filling

**Answer:** Based on the provided recipes, there is no chocolate pie that has dairy sour cream stirred into the cooked filling.

**Scores:** rr 0.00 · faithfulness 0.000 · answer_relevancy 0.850 · context_precision 0.250 · context_recall 0.400

### q018 — miss — gold [13619]

**Q:** Which peanut butter pie is a no-bake frozen pie made with cream cheese and whipped topping in a chocolate crumb crust?

**Reference:** Beat 1/3 cup creamy peanut butter with a 3-oz package of cream cheese and 2 tablespoons butter until smooth. Add confectioners sugar and milk, fold in an 8-oz carton of whipped topping, and pour into a chocolate crumb crust. Freeze at least 4 hours and serve frozen.

**Retrieved:** [37371] No Bake Peanut Butter Pie · [42249] Peanut Butter Pie (No Bake) · [22823] No Bake Peanut Butter Pie · [16229] Southern Peanut Butter Pie

**Answer:** Based on the recipes provided, there is no recipe that specifies using a chocolate crumb crust. The available crust options are graham cracker pie crust or a general baked pie shell.

**Scores:** rr 0.00 · faithfulness 1.000 · answer_relevancy 0.629 · context_precision 0.250 · context_recall 0.333

### q019 — miss — gold [5518, 21571]

**Q:** Which pumpkin bread is sweetened with molasses?

**Reference:** Combine the dry ingredients — whole wheat flour, sugar, salt, soda, baking powder, ginger, and nutmeg — then stir in 2/3 cup molasses, 2 cups pumpkin, a can of condensed milk, vanilla, and eggs. Pour into 2 greased loaf pans and bake at 350 degrees for 40 to 50 minutes.

**Retrieved:** [4507] Molasses Bars · [4262] Old-Time Molasses Cake · [47908] Festive Pumpkin Or Sweet Potato Bread · [38526] Molasses Doughnuts

**Answer:** Based on the provided recipes, the **Festive Pumpkin Or Sweet Potato Bread** uses sugar as its sweetener and does not list molasses as an ingredient.

**Scores:** rr 0.00 · faithfulness 1.000 · answer_relevancy 0.859 · context_precision 0.000 · context_recall 0.250

### q020 — hit — gold [36223, 44082]

**Q:** Which cheese ball is a sweet dessert version with crushed pineapple, maraschino cherries, and pecans?

**Reference:** Beat cream cheese with well-drained crushed pineapple and chopped maraschino cherries (plus a little chopped sweet pepper, onion, and salt), mold into a ball, and refrigerate overnight. Roll it in chopped pecans before serving.

**Retrieved:** [36223] Cheese Ball · [49371] Cheese Ball · [22488] Pineapple Cheese Ball · [48056] Cheese Ball

**Answer:** The cheese ball that includes crushed pineapple, maraschino cherries, and pecans is the **Cheese Ball** (Recipe 1).

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.915 · context_precision 0.917 · context_recall 1.000

### q021 — hit — gold [14709, 31605]

**Q:** Which meat loaf is mixed and topped with mozzarella and Cheddar cheese and bound with tomato soup and stuffing?

**Reference:** Mix 1 1/2 lb hamburger with a handful of stuffing, a can of tomato paste, crushed crackers, chopped onion, half a can of tomato soup, and handfuls of mozzarella and Cheddar. Put it in a loaf pan, top with the rest of the tomato soup and more mozzarella, and bake at 350 degrees for 1 hour.

**Retrieved:** [14709] Meat Loaf · [27825] Meat Loaf · [10367] Double Cheese Meat Loaf · [18682] Meat Loaf

**Answer:** The meat loaf that is mixed and topped with Mozzarella and Cheddar cheese, bound with tomato soup, and includes stuffing is the **Meat Loaf** (the first recipe listed).

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.833 · context_precision 1.000 · context_recall 1.000

### q022 — miss — gold [16875, 47550]

**Q:** Which sugar cookies are made with dairy sour cream in the dough?

**Reference:** Cream 1 cup shortening with 1 cup sugar, then add 1 cup dairy sour cream, 3 beaten egg yolks, and vanilla. Sift together flour, salt, baking soda, and baking powder, blend into the creamed mixture, chill, shape into balls, and bake.

**Retrieved:** [28262] Sour Cream Sugar Cookie · [16087] Sour Milk Cookies · [39470] Sour Cream Softies · [14433] Sour Cream Cookies

**Answer:** The sugar cookies made with dairy sour cream in the dough are the **Sour Cream Softies**.

**Scores:** rr 0.00 · faithfulness 1.000 · answer_relevancy 0.913 · context_precision 0.333 · context_recall 0.286

### q023 — hit — gold [9692, 11414, 29900]

**Q:** Which pound cake has crushed pineapple and candied cherries folded into the batter?

**Reference:** Cream 3 sticks of oleo with 6 eggs added one at a time, then beat in vanilla and a 1-lb box of powdered sugar. Gradually add flour, baking powder, chopped nuts, drained crushed pineapple, and candied cherries, and bake in a greased tube pan at 350 degrees for about 1 hour and 10 minutes.

**Retrieved:** [35427] Pineapple Upside-Down Pound Cake · [9692] Pound Cake · [46018] Pineapple Pound Cake · [42113] Pineapple Pound Cake

**Answer:** The recipe for **Pound Cake** includes both crushed pineapple, drained, and candied cherries in its ingredients list, which are added when you gradually add "flour and fruit" to the batter.

**Scores:** rr 0.50 · faithfulness 1.000 · answer_relevancy 0.828 · context_precision 0.500 · context_recall 1.000

### q024 — hit — gold [8328]

**Q:** Which chili is thickened with a couple of handfuls of oatmeal and includes cocoa?

**Reference:** Cook 5 lb coarse ground beef, then add a 64-oz can of tomato juice, salt, sugar, chili seasoning (Williams), and 3 cans of beans, and simmer about 20 minutes. Add chopped garlic and cook 5 minutes more, then stir in 3 tablespoons cocoa and a couple of handfuls of oatmeal and cook until the oatmeal disappears.

**Retrieved:** [8328] Chili · [5141] Chili · [2607] Mexican-Style Hot Chocolate · [14881] Chili

**Answer:** The chili that includes both cocoa and oatmeal is the first recipe listed as **Chili**. This recipe requires adding cocoa and oatmeal near the end of the cooking process, continuing to cook until the oatmeal disappears.

**Scores:** rr 1.00 · faithfulness 1.000 · answer_relevancy 0.858 · context_precision 1.000 · context_recall 1.000

