import random

from django.utils import timezone

from apps.users.models import User
from apps.cuisine_types.models import CuisineType
from apps.ingredients.models import Ingredient, Category
from apps.meal_types.models import MealType
from apps.recipes.models import Recipe, RecipeIngredient

def create_initial_users(users):
    for user_data in users:
        user = User.objects.create(
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            is_active=user_data.get('is_active', True),
            is_superuser=user_data.get('is_superuser', False),
            is_staff=user_data.get('is_staff', False),
            date_joined=timezone.now() if 'date_joined' not in user_data else user_data['date_joined']
        )
        user.set_password('nutricook')
        user.save()

users = [
    {
        "username": "user1",
        "first_name": "John",
        "last_name": "Doe",
        "email": "user1@example.com",
        "date_joined": "2023-01-01T00:00:00Z"
    },
    {
        "username": "user2",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "user2@example.com",
        "date_joined": "2023-01-02T00:00:00Z"
    }
]

create_initial_users(users)



def populate_cuisine_types():
    cuisine_types = ['Italian', 'Mexican', 'Chinese', 'Indian', 'Japanese', 'French', 'Mediterranean', 'Thai', 'Greek', 'American']
    for cuisine in cuisine_types:
        CuisineType.objects.get_or_create(name=cuisine)

def populate_meal_types():
    meal_types = ['Breakfast', 'Brunch', 'Lunch', 'Dinner', 'Snack']
    for meal in meal_types:
        MealType.objects.get_or_create(name=meal)

def populate_ingredients():
    ingredients = [
        {'name': 'Tomato', 'category': 'Vegetable'},
        {'name': 'Onion', 'category': 'Vegetable'},
        {'name': 'Chicken', 'category': 'Meat'},
        {'name': 'Rice', 'category': 'Grains'},
        {'name': 'Garlic', 'category': 'Vegetable'},
        {'name': 'Beef', 'category': 'Meat'},
        {'name': 'Pasta', 'category': 'Grains'},
        {'name': 'Potato', 'category': 'Vegetable'},
        {'name': 'Lettuce', 'category': 'Vegetable'},
        {'name': 'Egg', 'category': 'Dairy'},
        {'name': 'Milk', 'category': 'Dairy'},
        {'name': 'Carrot', 'category': 'Vegetable'},
        {'name': 'Fish', 'category': 'Seafood'},
        {'name': 'Lemon', 'category': 'Fruit'},
        {'name': 'Orange', 'category': 'Fruit'},
        {'name': 'Apple', 'category': 'Fruit'},
        {'name': 'Banana', 'category': 'Fruit'},
        {'name': 'Spinach', 'category': 'Vegetable'},
        {'name': 'Broccoli', 'category': 'Vegetable'},
        {'name': 'Cheese', 'category': 'Dairy'},
        {'name': 'Pork', 'category': 'Meat'},
        {'name': 'Turkey', 'category': 'Meat'},
        {'name': 'Cucumber', 'category': 'Vegetable'},
        {'name': 'Bell Pepper', 'category': 'Vegetable'},
        {'name': 'Zucchini', 'category': 'Vegetable'},
        {'name': 'Strawberry', 'category': 'Fruit'},
        {'name': 'Blueberry', 'category': 'Fruit'},
        {'name': 'Raspberry', 'category': 'Fruit'},
        {'name': 'Avocado', 'category': 'Fruit'},
        {'name': 'Celery', 'category': 'Vegetable'},
        {'name': 'Green Beans', 'category': 'Vegetable'},
        {'name': 'Soy Sauce', 'category': 'Condiments'},
        {'name': 'Olive Oil', 'category': 'Condiments'},
        {'name': 'Vinegar', 'category': 'Condiments'},
        {'name': 'Honey', 'category': 'Condiments'},
        {'name': 'Sugar', 'category': 'Condiments'},
        {'name': 'Salt', 'category': 'Condiments'},
        {'name': 'Pepper', 'category': 'Condiments'},
        {'name': 'Cinnamon', 'category': 'Condiments'},
        {'name': 'Ginger', 'category': 'Condiments'},
        {'name': 'Soy Milk', 'category': 'Dairy'},
        {'name': 'Almond Milk', 'category': 'Dairy'},
        {'name': 'Coconut Milk', 'category': 'Dairy'},
        {'name': 'Cashew Milk', 'category': 'Dairy'},
        {'name': 'Cheddar Cheese', 'category': 'Dairy'},
        {'name': 'Mozzarella Cheese', 'category': 'Dairy'},
        {'name': 'Parmesan Cheese', 'category': 'Dairy'},
        {'name': 'Feta Cheese', 'category': 'Dairy'},
        {'name': 'Salmon', 'category': 'Seafood'},
        {'name': 'Shrimp', 'category': 'Seafood'},
        {'name': 'Tuna', 'category': 'Seafood'},
        {'name': 'Crab', 'category': 'Seafood'},
        {'name': 'Lobster', 'category': 'Seafood'},
        {'name': 'Peanut Butter', 'category': 'Condiments'},
        {'name': 'Ketchup', 'category': 'Condiments'},
        {'name': 'Mustard', 'category': 'Condiments'},
        {'name': 'Mayonnaise', 'category': 'Condiments'},
        {'name': 'Soybeans', 'category': 'Legumes'},
        {'name': 'Black Beans', 'category': 'Legumes'},
        {'name': 'Chickpeas', 'category': 'Legumes'},
        {'name': 'Lentils', 'category': 'Legumes'},
        {'name': 'Quinoa', 'category': 'Grains'},
        {'name': 'Barley', 'category': 'Grains'},
        {'name': 'Oats', 'category': 'Grains'},
        {'name': 'Corn', 'category': 'Grains'},
        {'name': 'Artichoke', 'category': 'Vegetable'},
        {'name': 'Asparagus', 'category': 'Vegetable'},
        {'name': 'Eggplant', 'category': 'Vegetable'},
        {'name': 'Cauliflower', 'category': 'Vegetable'},
        {'name': 'Brussels Sprouts', 'category': 'Vegetable'},
        {'name': 'Grapefruit', 'category': 'Fruit'},
        {'name': 'Pineapple', 'category': 'Fruit'},
        {'name': 'Watermelon', 'category': 'Fruit'},
        {'name': 'Kiwi', 'category': 'Fruit'},
        {'name': 'Cantaloupe', 'category': 'Fruit'},
        {'name': 'Honeydew', 'category': 'Fruit'},
        {'name': 'Mango', 'category': 'Fruit'},
        {'name': 'Peach', 'category': 'Fruit'},
        {'name': 'Pear', 'category': 'Fruit'},
        {'name': 'Plum', 'category': 'Fruit'},
        {'name': 'Cherry', 'category': 'Fruit'},
        {'name': 'Pomegranate', 'category': 'Fruit'},
        {'name': 'Raisins', 'category': 'Dried Fruits'},
        {'name': 'Dates', 'category': 'Dried Fruits'},
        {'name': 'Prunes', 'category': 'Dried Fruits'},
        {'name': 'Apricots', 'category': 'Dried Fruits'},
        {'name': 'Cranberries', 'category': 'Dried Fruits'},
        {'name': 'Currants', 'category': 'Dried Fruits'},
        {'name': 'Fig', 'category': 'Dried Fruits'},
        {'name': 'Apple Cider Vinegar', 'category': 'Condiments'},
        {'name': 'Balsamic Vinegar', 'category': 'Condiments'},
        {'name': 'White Vinegar', 'category': 'Condiments'},
        {'name': 'Red Wine Vinegar', 'category': 'Condiments'},
        {'name': 'Apple Juice', 'category': 'Beverages'},
        {'name': 'Orange Juice', 'category': 'Beverages'},
        {'name': 'Cranberry Juice', 'category': 'Beverages'},
        {'name': 'Grape Juice', 'category': 'Beverages'},
        {'name': 'Pineapple Juice', 'category': 'Beverages'},
        {'name': 'Lime Juice', 'category': 'Beverages'},
        {'name': 'Lemon Juice', 'category': 'Beverages'},
        {'name': 'Ginger Ale', 'category': 'Beverages'},
        {'name': 'Club Soda', 'category': 'Beverages'},
        {'name': 'Tonic Water', 'category': 'Beverages'},
        {'name': 'Coca-Cola', 'category': 'Sodas'},
        {'name': 'Pepsi', 'category': 'Sodas'},
        {'name': 'Sprite', 'category': 'Sodas'},
        {'name': 'Mountain Dew', 'category': 'Sodas'},
        {'name': 'Dr. Pepper', 'category': 'Sodas'},
        {'name': '7-Up', 'category': 'Sodas'},
        {'name': 'Root Beer', 'category': 'Sodas'},
        {'name': 'Cream Soda', 'category': 'Sodas'},
        {'name': 'Ginger Beer', 'category': 'Sodas'},
        {'name': 'Iced Tea', 'category': 'Teas'},
        {'name': 'Green Tea', 'category': 'Teas'},
        {'name': 'Black Tea', 'category': 'Teas'},
        {'name': 'White Tea', 'category': 'Teas'},
        {'name': 'Chamomile Tea', 'category': 'Teas'},
        {'name': 'Peppermint Tea', 'category': 'Teas'},
        {'name': 'Lavender Tea', 'category': 'Teas'},
        {'name': 'Earl Grey Tea', 'category': 'Teas'},
        {'name': 'Oolong Tea', 'category': 'Teas'},
        {'name': 'Matcha Tea', 'category': 'Teas'},
        {'name': 'Chai Tea', 'category': 'Teas'},
        {'name': 'Hibiscus Tea', 'category': 'Teas'},
        {'name': 'Rooibos Tea', 'category': 'Teas'},
        {'name': 'Yerba Mate Tea', 'category': 'Teas'},
        {'name': 'Soy Sauce', 'category': 'Condiments'},
        {'name': 'Fish Sauce', 'category': 'Condiments'},
        {'name': 'Hoisin Sauce', 'category': 'Condiments'},
        {'name': 'Oyster Sauce', 'category': 'Condiments'},
        {'name': 'Worcestershire Sauce', 'category': 'Condiments'},
        {'name': 'Tahini', 'category': 'Condiments'},
        {'name': 'Sesame Oil', 'category': 'Condiments'},
        {'name': 'Tabasco Sauce', 'category': 'Condiments'},
        {'name': 'Sriracha Sauce', 'category': 'Condiments'},
        {'name': 'Wasabi', 'category': 'Condiments'},
        {'name': 'Mirin', 'category': 'Condiments'},
        {'name': 'Sake', 'category': 'Condiments'},
        {'name': 'Vermouth', 'category': 'Condiments'},
        {'name': 'Maraschino Cherry', 'category': 'Condiments'},
        {'name': 'Simple Syrup', 'category': 'Condiments'},
        {'name': 'Agave Nectar', 'category': 'Condiments'},
        {'name': 'Maple Syrup', 'category': 'Condiments'},
        {'name': 'Wheat Flour', 'category': 'Baking'},
        {'name': 'All-Purpose Flour', 'category': 'Baking'},
        {'name': 'Cornstarch', 'category': 'Baking'},
        {'name': 'Baking Powder', 'category': 'Baking'},
        {'name': 'Baking Soda', 'category': 'Baking'},
        {'name': 'Cocoa Powder', 'category': 'Baking'},
        {'name': 'Vanilla Extract', 'category': 'Baking'},
        {'name': 'Almond Extract', 'category': 'Baking'},
        {'name': 'Coconut Extract', 'category': 'Baking'},
        {'name': 'Orange Extract', 'category': 'Baking'},
        {'name': 'Lemon Extract', 'category': 'Baking'},
        {'name': 'Cream of Tartar', 'category': 'Baking'},
        {'name': 'Shortening', 'category': 'Baking'},
        {'name': 'Butter', 'category': 'Dairy'},
        {'name': 'Margarine', 'category': 'Dairy'},
        {'name': 'Heavy Cream', 'category': 'Dairy'},
        {'name': 'Whipped Cream', 'category': 'Dairy'},
        {'name': 'Half-and-Half', 'category': 'Dairy'},
        {'name': 'Condensed Milk', 'category': 'Dairy'},
        {'name': 'Evaporated Milk', 'category': 'Dairy'},
        {'name': 'Coconut Cream', 'category': 'Dairy'},
        {'name': 'Powdered Milk', 'category': 'Dairy'},
        {'name': 'Ice Cream', 'category': 'Dairy'},
        {'name': 'Sherbet', 'category': 'Dairy'},
        {'name': 'Yogurt', 'category': 'Dairy'},
        {'name': 'Sour Cream', 'category': 'Dairy'},
        {'name': 'Cottage Cheese', 'category': 'Dairy'},
        {'name': 'Ricotta Cheese', 'category': 'Dairy'},
        {'name': 'Mascarpone Cheese', 'category': 'Dairy'},
        {'name': 'Soy Yogurt', 'category': 'Dairy'},
        {'name': 'Almond Yogurt', 'category': 'Dairy'},
        {'name': 'Coconut Yogurt', 'category': 'Dairy'},
        {'name': 'Cashew Yogurt', 'category': 'Dairy'},
        {'name': 'Blue Cheese', 'category': 'Dairy'},
        {'name': 'Gorgonzola Cheese', 'category': 'Dairy'},
        {'name': 'Roquefort Cheese', 'category': 'Dairy'},
        {'name': 'Bleu Cheese', 'category': 'Dairy'},
        {'name': 'Goat Cheese', 'category': 'Dairy'},
        {'name': 'Brie Cheese', 'category': 'Dairy'},
        {'name': 'Camembert Cheese', 'category': 'Dairy'},
        {'name': 'Gouda Cheese', 'category': 'Dairy'},
        {'name': 'Edam Cheese', 'category': 'Dairy'},
        {'name': 'Havarti Cheese', 'category': 'Dairy'},
        {'name': 'Monterey Jack Cheese', 'category': 'Dairy'},
        {'name': 'Muenster Cheese', 'category': 'Dairy'},
        {'name': 'Pepper Jack Cheese', 'category': 'Dairy'},
        {'name': 'Provolone Cheese', 'category': 'Dairy'},
        {'name': 'Swiss Cheese', 'category': 'Dairy'},
        {'name': 'American Cheese', 'category': 'Dairy'},
        {'name': 'Cheddar Jack Cheese', 'category': 'Dairy'},
        {'name': 'Colby Cheese', 'category': 'Dairy'},
        {'name': 'Colby Jack Cheese', 'category': 'Dairy'},
        {'name': 'Farmers Cheese', 'category': 'Dairy'},
        {'name': 'Fontina Cheese', 'category': 'Dairy'},
    ]
    for ingredient in ingredients:
        category_name = ingredient.pop('category')
        category, _ = Category.objects.get_or_create(name=category_name)
        Ingredient.objects.get_or_create(category=category, **ingredient)


populate_cuisine_types()
populate_meal_types()
populate_ingredients()


cuisine_types = ['Italian', 'Mexican', 'Chinese', 'Indian', 'Japanese', 'French', 'Mediterranean', 'Thai', 'Greek', 'American']
for cuisine_type in cuisine_types:
    CuisineType.objects.get_or_create(name=cuisine_type)

ingredients = Ingredient.objects.all()

cuisine_types = CuisineType.objects.all()

users = User.objects.all()

recipe_titles = [
    "Spicy Chicken Tacos",
    "Creamy Mushroom Risotto",
    "Tangy Lemon Herb Salmon",
    "Garlic Butter Shrimp Pasta",
    "Mediterranean Quinoa Salad",
    "Thai Red Curry Chicken",
    "Caprese Stuffed Portobello Mushrooms",
    "BBQ Pulled Pork Sandwiches",
    "Veggie-packed Chicken Stir-fry",
    "Sweet and Sour Pineapple Chicken",
    "Greek-style Grilled Lamb Chops",
    "Creamy Pesto Chicken Pasta",
    "Teriyaki Glazed Salmon",
    "Cajun Shrimp and Sausage Skillet",
    "Mushroom and Spinach Stuffed Chicken Breast",
    "Italian Sausage and Peppers Pasta",
    "Honey Mustard Glazed Pork Tenderloin",
    "Vegetable Tikka Masala",
    "Lemon Garlic Butter Scallops",
    "Mexican Street Corn Salad"
]

for i in range(30):
    user = random.choice(users)
    cuisine_type = random.choice(cuisine_types)
    recipe_title = random.choice(recipe_titles)
    recipe_description = f"Description for {recipe_title}"
    recipe = Recipe.objects.create(title=recipe_title, description=recipe_description, author=user, cuisine_type=cuisine_type)
    num_ingredients = random.randint(3, 5)
    selected_ingredients = random.sample(list(ingredients), num_ingredients)
    for ingredient in selected_ingredients:
        quantity = round(random.uniform(0.1, 2.0), 2)
        unit = random.choice(['g', 'kg', 'ml', 'L', 'tsp', 'tbsp'])
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity, unit=unit)