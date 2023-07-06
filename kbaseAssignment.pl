servesAll(american, [salad, steak, sandwiches, burgers, fried_chicken]).
servesAll(burger_place, [burgers, fries, onion_rings]).
servesAll(chinese, [eggrolls, rice, shrimp, soup, noodles]).
servesAll(indian, [papadam, bagan, bharta, rice, tandoori, naan]).
serveAll(italian, [salad, pasta, cioppino, snapper, bread, garlic_bread]).
servesAll(japanese, [sashimi, rice, tempura, noodles]).
servesAll(mediterranean, [gyros, hummus, pita, falafel]).
servesAll(mexican, [tacos, beans, rice, enchiladas, fish_tacos]).
servesAll(pizza_place, [pizza, salad, garlic_bread]).
servesAll(thai, [rice, noodles, larb, pad_thai]).

dish(vegetarian[beans, bagan_bharta, enchiladas, falafel, hummas, pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).
dish(meat[burgers, enchiladas, gyros, pad_thai, pizza, steak, sandwiches, fried_chicken, tacos, tandoori, larb]).
dish(seafood[snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]).
dish(starch[naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).

cuisine(american, [waterman_grille, red_stripe]).
cuisine(burger_place, [shake_shack]).
cuisine(chinese, [yans, chinatown]).
cuisine(indian, [kabob_n_curry]).
cusine(italian, [pasta_beach, al_frono]).
cusine(japanese,[haruki]).
cusine(mediterranean, [andreas, east_side_pocokets]).
cusine(mexican, [bajas, dolores, tallulahs]).
cusine(pizza_place,[pizza_marvin, mikes]).
cuisine(thai, [heng, bees, lims]).

location(thayer_street, [yans, andreas, chindatown, kabob_n_curry, mikes, east_side_pocokets, shake_shack]).
location(fox_point, [pizza_marvin, dolores, bees, al_frono]).
location(wayland, [waterman_grille, tallulahs, red_stripe, haruki, lims]).



serves(Kind, Dish):-
    servesAll(Kind, Dish)
    member (Dish, Dishes)





