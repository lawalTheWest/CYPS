# app/crops.py

crops = {
        # The Wheat
        "wheat": {
            "scientific_name": "Triticum spp.",
            "description": "Wheat is a cereal grain originally from the Levant region of the Near East and Ethiopian Highlands. It is now cultivated worldwide.",
            "uses": ["Human consumption as flour, bread, pasta", "Animal feed", "Alcoholic beverages"],
            "nutritional_value": {
                "calories": 327,
                "carbohydrates": 71.2,
                "protein": 12.6,
                "fat": 1.5,
                "fiber": 12.2
                },
            "growing_conditions": {
                "temperature": "15-25°C (59-77°F)",
                "rainfall": "300-900 mm",
                "soil": "Loamy soil with good drainage"
                },
            "image": "wheat.jpg" # updated this line of code to include the images
            },

        # The Corn
        "corn": {
            "scientific_name": "Zea mays",
            "description": "Corn, also known as maize, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago.",
            "uses": ["Human consumption as grain, flour, oil", "Animal feed", "Biofuel production"],
            "nutritional_value": {
                "calories": 365,
                "carbohydrates": 74.3,
                "protein": 9.4,
                "fat": 4.7,
                "fiber": 7.3
                },
            "growing_conditions": {
                "temperature": "18-27°C (64-81°F)",
                "rainfall": "400-800 mm",
                "soil": "Well-drained, fertile soil"
                }
            "image": "corn.jpg"
            },

        # The Rice
        "rice": {
            "scientific_name": "Oryza sativa",
            "description": "Rice is a staple food for over half of the world's population. It is a cereal grain that is cultivated worldwide.",
            "uses": ["Human consumption as grain, flour, and various rice products"],
            "nutritional_value": {
                "calories": 130,
                "carbohydrates": 28,
                "protein": 2.7,
                "fat": 0.3,
                "fiber": 0.4
                },
            "growing_conditions": {
                "temperature": "20-30°C (68-86°F)",
                "rainfall": "1200-1500 mm",
                "soil": "Heavy soils with good water retention"
                }
            "image": "rice.jpg" # display
            },

        # The Yam
        "yam": {
                "scientific_name": "Dioscorea spp.",
                "description": "Yam is a starchy tuber that is an important food crop in many parts of the world.",
                "uses": ["Human consumption as boiled, roasted, or fried tubers", "Flour"],
                "nutritional_value": {
                    "calories": 118,
                    "carbohydrates": 27.9,
                    "protein": 1.5,
                    "fat": 0.2,
                    "fiber": 4.1
                    },
                "growing_conditions": {
                    "temperature": "25-30°C (77-86°F)",
                    "rainfall": "1000-1500 mm",
                    "soil": "Well-drained, sandy loam soil"
                    }
                "image": "yam.jpg" # display 
                },

        # The Cassava
        "cassava": {
                "scientific_name": "Manihot esculenta",
                "description": "Cassava is a root vegetable that is a major source of carbohydrates in tropical regions.",
                "uses": ["Human consumption as boiled, fried, or processed into flour", "Animal feed"],
                "nutritional_value": {
                    "calories": 160,
                    "carbohydrates": 38.1,
                    "protein": 1.4,
                    "fat": 0.3,
                    "fiber": 1.8
                    },
                "growing_conditions": {
                    "temperature": "25-29°C (77-84°F)",
                    "rainfall": "1000-1500 mm",
                    "soil": "Well-drained, sandy loam or loamy soil"
                    }
                "image": "cassava.jpg" # The display
                },

        # The Carrot
        "carrot": {
                "scientific_name": "Daucus carota",
                "description": "Carrot is a root vegetable that is commonly consumed worldwide.",
                "uses": ["Human consumption as raw, cooked, or processed into juice and other products"],
                "nutritional_value": {
                    "calories": 41,
                    "carbohydrates": 9.6,
                    "protein": 0.9,
                    "fat": 0.2,
                    "fiber": 2.8
        },
                "growing_conditions": {
                    "temperature": "16-21°C (60-70°F)",
                    "rainfall": "600-800 mm",
                    "soil": "Loose, sandy loam soil with good drainage"
                    }
                "image": "carrot.jpg" # The carrot display
                },

        # The tomatoes plant
        "tomatoes": {
                "scientific_name": "Solanum lycopersicum",
                "description": "Tomato is a widely cultivated fruit that is used as a vegetable in cooking.",
                "uses": ["Human consumption as fresh, cooked, or processed into sauce, juice, and other products"],
                "nutritional_value": {
                    "calories": 18,
                    "carbohydrates": 3.9,
                    "protein": 0.9,
                    "fat": 0.2,
                    "fiber": 1.2
                    },
                "growing_conditions": {
                    "temperature": "20-24°C (68-75°F)",
                    "rainfall": "400-600 mm",
                    "soil": "Well-drained, fertile soil with organic matter"
                    }
                "image": "tomatoes.jpg" # The tomatoes plant display
                },

        # The beans plant
        "beans": {
                "scientific_name": "Phaseolus vulgaris",
                "description": "Beans are legumes that are widely cultivated for their edible seeds.",
                "uses": ["Human consumption as cooked beans, flour, and other products"],
                "nutritional_value": {
                    "calories": 347,
                    "carbohydrates": 62.5,
                    "protein": 21.4,
                    "fat": 1.2,
                    "fiber": 15.2
                    },
                "growing_conditions": {
                    "temperature": "18-24°C (64-75°F)",
                    "rainfall": "400-600 mm",
                    "soil": "Well-drained, fertile soil with organic matter"
                    }
                "image": "beans.jpg" # The beans plant
                },

        # The groundnut plant
        "groundnut": {
                "scientific_name": "Arachis hypogaea",
                "description": "Groundnut, also known as peanut, is a legume crop grown mainly for its edible seeds.",
                "uses": ["Human consumption as roasted nuts, peanut butter, oil, and other products"],
                "nutritional_value": {
                    "calories": 567,
                    "carbohydrates": 16.1,
                    "protein": 25.8,
                    "fat": 49.2,
                    "fiber": 8.5
                    },
                "growing_conditions": {
                    "temperature": "20-30°C (68-86°F)",
                    "rainfall": "500-1000 mm",
                    "soil": "Light, sandy loam soil with good drainage"
                    }
                "image": "groundnut.jpg" # the groundnut display
                }
        # To increase the crops i could add them in this section...
        }
