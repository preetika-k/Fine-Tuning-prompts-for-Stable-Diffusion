stop_token = ["paragraph:"]

paragraph = "The ocean is also a beautiful and serene place. The waves crashing on the shore, the sound of the seagulls, and the smell of the salty air can all be very calming. One of the most scenic aspects of the ocean is its fish. There are thousands of different species of fish in the ocean, each with its own unique colors and patterns. The waves can be gentle and calming, or they can be powerful and crashing."
"Hello world!\""

prompt = f"""
paragraph: The first light of the golden sun peeked over the jagged peaks of the distant mountains, casting a warm glow over the lush valley below. A gentle breeze danced through the trees, rustling their leaves and carrying the sweet scent of wildflowers. In the distance, a sparkling river meandered through the landscape, its waters reflecting the azure sky above.
sd_prompt: Sharp, jagged mountains with snow-capped peaks, lush green valley, clear river winding through the valley, forest with wildflowers, waterfall, golden sunlight, realistic

paragraph: 
The Moon is a barren and desolate landscape, devoid of air or liquid water. Its surface is covered in craters, formed by impacts from asteroids and comets over billions of years.The largest craters are hundreds of miles wide and have towering mountains along their rims.The Moon's surface is also covered in a layer of fine dust, called regolith. This dust is made up of crushed rock and glass, and it gives the Moon its characteristic gray appearance.
sd_prompt: black skies, big craters, gray aura, bright stars, dusty rocks, high-quality image, realistic, vibrant

paragraph: A narrow alleyway winds through the village, past small shops and restaurants. The village square is a popular gathering place, where locals and visitors alike come to enjoy theviews and the relaxed atmosphere. Manarola is a picturesque village perched on a cliffside overlooking the Ligurian Sea. It is one of the five villages that make up the Cinque Terre, a UNESCO World Heritage Site. Manarola is known for its colorful houses, which cascade down the hillside to the sea.
sd_prompt: seaside, vibrant colorful apartment houses, narrow cobblestone paths, small shops, restaurants, impressionism

paragraph:{paragraph}
sd_prompt:"""



output = "sd_prompt paragraph:"

#prompt
print(prompt)
prompt = sd_prompt
