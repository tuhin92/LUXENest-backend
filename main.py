from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/data", methods=['GET'])
def data():
    return jsonify(
        [
    {
      "id": 1,
      "name": "Luxury Villa with Ocean View",
      "price": "$1,500,000",
      "location": "Miami, Florida",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 2,
      "name": "Modern Apartment in City Center",
      "price": "$800,000",
      "location": "New York City, NY",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 3,
      "name": "Cozy Cottage in the Countryside",
      "price": "$400,000",
      "location": "Cotswolds, UK",
      "image": "https://i.ibb.co/mNY4t8s/pexels-max-vakhtbovycn-7061672.jpg"
    },
    {
      "id": 4,
      "name": "Spacious Family Home with Garden",
      "price": "$600,000",
      "location": "Los Angeles, CA",
      "image": "https://i.ibb.co/mNY4t8s/pexels-max-vakhtbovycn-7061672.jpg"
    },
    {
      "id": 5,
      "name": "Luxury Condo with Panoramic Views",
      "price": "$1,200,000",
      "location": "Chicago, IL",
      "image": "https://i.ibb.co/J3SLdf3/pexels-max-vakhtbovycn-6580215.jpg"
    },
    {
      "id": 6,
      "name": "Modern Loft in Artsy Neighborhood",
      "price": "$900/month",
      "location": "San Francisco, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 7,
      "name": "Beachfront Bungalow with Private Pool",
      "price": "$1,800,000",
      "location": "Maui, Hawaii",
      "image": "https://i.ibb.co/B48fmQY/pexels-pixabay-210265.jpg"
    },
    {
      "id": 8,
      "name": "Rustic Cabin Retreat in the Mountains",
      "price": "$700,000",
      "location": "Aspen, Colorado",
      "image": "https://i.ibb.co/PCr5qSd/pexels-kamo11235-667838.jpg"
    },
    {
      "id": 9,
      "name": "Historic Mansion with Garden",
      "price": "$2,500,000",
      "location": "Charleston, SC",
      "image": "https://i.ibb.co/W6HXmRF/pexels-asadphoto-1268855.jpg"
    },
    {
      "id": 10,
      "name": "Contemporary Townhouse with Rooftop Terrace",
      "price": "$1,100,000",
      "location": "Seattle, WA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 11,
      "name": "Mountain View Chalet with Hot Tub",
      "price": "$1,300,000",
      "location": "Banff, Canada",
      "image": "https://i.ibb.co/P5CxVXr/pexels-pixabay-210552.jpg"
    },
    {
      "id": 12,
      "name": "Gorgeous Lakeside Retreat",
      "price": "$950,000",
      "location": "Lake Tahoe, CA",
      "image": "https://i.ibb.co/J3SLdf3/pexels-max-vakhtbovycn-6580215.jpg"
    },
    {
      "id": 13,
      "name": "Charming Tudor-style Home",
      "price": "$850,000",
      "location": "Princeton, NJ",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 14,
      "name": "Sleek Urban Loft with City Views",
      "price": "$1,000,000",
      "location": "Portland, OR",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 15,
      "name": "Classic Colonial Home with Pool",
      "price": "$1,700,000",
      "location": "Boston, MA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 16,
      "name": "Ranch-style Retreat in the Desert",
      "price": "$750,000",
      "location": "Scottsdale, AZ",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 17,
      "name": "Secluded Mountain Hideaway",
      "price": "$1,250,000",
      "location": "Jackson Hole, WY",
      "image": "https://i.ibb.co/P5CxVXr/pexels-pixabay-210552.jpg"
    },
    {
      "id": 18,
      "name": "Chic Loft in Historic District",
      "price": "$850,000",
      "location": "Savannah, GA",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 19,
      "name": "Contemporary Beach House with Infinity Pool",
      "price": "$2,200,000",
      "location": "Malibu, CA",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 20,
      "name": "Majestic Mansion with Oceanfront Views",
      "price": "$3,000,000",
      "location": "Hamptons, NY",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 21,
      "name": "Picturesque Cottage with Garden",
      "price": "$550,000",
      "location": "Carmel-by-the-Sea, CA",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 22,
      "name": "Elegant Victorian Home with Wraparound Porch",
      "price": "$1,450,000",
      "location": "Nashville, TN",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 23,
      "name": "Urban Penthouse with Skyline Views",
      "price": "$2,500,000",
      "location": "Miami, Florida",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 24,
      "name": "Quaint Farmhouse in Wine Country",
      "price": "$950,000",
      "location": "Napa Valley, CA",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 25,
      "name": "Luxury Penthouse with Private Elevator",
      "price": "$3,500,000",
      "location": "Manhattan, NY",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 26,
      "name": "Charming Craftsman Bungalow",
      "price": "$650,000",
      "location": "Portland, OR",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 27,
      "name": "Spectacular Cliffside Estate",
      "price": "$4,000,000",
      "location": "Big Sur, CA",
      "image": "https://i.ibb.co/qD63f93/pexels-pixabay-276551.jpg"
    },
    {
      "id": 28,
      "name": "Elegant French Chateau",
      "price": "$6,500,000",
      "location": "Montecito, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 29,
      "name": "Chic City Loft with Industrial Charm",
      "price": "$1,200,000",
      "location": "Brooklyn, NY",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 30,
      "name": "Tropical Paradise Villa",
      "price": "$2,800,000",
      "location": "Key West, FL",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 31,
      "name": "Spanish Colonial Revival Mansion",
      "price": "$3,750,000",
      "location": "Santa Barbara, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 32,
      "name": "Modern Riverside Retreat",
      "price": "$1,850,000",
      "location": "Austin, TX",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 33,
      "name": "Sleek Minimalist Apartment",
      "price": "$950,000",
      "location": "San Diego, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 34,
      "name": "Coastal Cottage with Panoramic Ocean Views",
      "price": "$1,950,000",
      "location": "Monterey, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 35,
      "name": "Mediterranean Villa with Infinity Pool",
      "price": "$2,300,000",
      "location": "Santa Monica, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 36,
      "name": "Secluded Beachfront Retreat",
      "price": "$2,600,000",
      "location": "Maui, Hawaii",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 37,
      "name": "Historic Colonial Estate",
      "price": "$4,250,000",
      "location": "Williamsburg, VA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 38,
      "name": "Luxury Ski Chalet",
      "price": "$5,500,000",
      "location": "Vail, CO",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 39,
      "name": "Modern Beachfront Villa",
      "price": "$3,200,000",
      "location": "Miami Beach, FL",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 40,
      "name": "French Riviera Luxury Estate",
      "price": "$9,000,000",
      "location": "Nice, France",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 41,
      "name": "Historic Brownstone in Park Slope",
      "price": "$1,750,000",
      "location": "Brooklyn, NY",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 42,
      "name": "Tuscan Villa with Vineyard",
      "price": "$6,200,000",
      "location": "Florence, Italy",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 43,
      "name": "Charming Victorian Cottage",
      "price": "$850,000",
      "location": "San Francisco, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 44,
      "name": "Sustainable Eco-Home",
      "price": "$1,100,000",
      "location": "Boulder, CO",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 45,
      "name": "Rustic Mountain Lodge",
      "price": "$1,300,000",
      "location": "Lake Placid, NY",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 46,
      "name": "Italian Countryside Villa",
      "price": "$4,500,000",
      "location": "Tuscany, Italy",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 47,
      "name": "Historic Southern Plantation",
      "price": "$3,800,000",
      "location": "Charleston, SC",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 48,
      "name": "Seaside Cottage with Lighthouse Views",
      "price": "$950,000",
      "location": "Cape Cod, MA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 49,
      "name": "Elegant Colonial Revival Mansion",
      "price": "$4,000,000",
      "location": "Georgetown, DC",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    },
    {
      "id": 50,
      "name": "Modern Desert Oasis",
      "price": "$1,700,000",
      "location": "Palm Springs, CA",
      "image": "https://i.ibb.co/XCrBPJ5/pexels-pixabay-280221.jpg"
    }
  ]

    )
if __name__ == "__main__":
    app.run(debug=True, port=8080)