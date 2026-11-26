import streamlit as st
from pathlib import Path
#project and image folder location
BASE_DIR=Path(__file__).resolve().parent
IMAGE_DIR=BASE_DIR / "images"

st.set_page_config(
    page_title="Karnataka TripMate",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Karnataka TripMate")
st.subheader("Your Personal Karnataka Travel Planner")

st.write(
    "plan your next trip around Karnataka based on"
    "your budget,duration,and interests!"
)
st.divider()

#plan your trip
st.header("✈️ Plan Your Trip ")

city=st.selectbox(
    "where are you travelling from?",
    ["Bengaluru","Mysuru","Hubballi","Mangaluru","other"]
)
budget=st.number_input(
    "Your total budget",
    min_value=500,
    max_value=100000,
    value=5000,
    step=500
)
days=st.selectbox(
    "How many days is your trip?",
    [1,2,3,4,5,6,7]
)
interests=st.multiselect(
    "What would you like to explore?",
    ["Natuure","Historical Places","Temples","Beaches","Adventure","wildlife"]
)
if st.button("Generate My Trip",type="primary"):
    st.subheader("Your Trip Summary")
    st.write(f"starting city:{city}")
    st.write(f"Total budget:{budget:,}")
    st.write(f"Duration:{days}day(s)")

    if interests:
        st.write("Interests: " + ",".join(interests))
    else:
        st.info("You haven't selected any interests yet.")
    st.success("Your trip preferences are ready!")
st.divider()
def find_image(stem):
    """Find an image file by its name,ignoring extension case."""
    for exit in (".jpg",".jpeg",".png",".JPG",".JPEG",".PNG"):
        path=IMAGE_DIR / F"{stem}{exit}"
        if path.is_file():
            return path
    return None

# Destination information (image=file name without extension)
destination={
    "Mysuru palace":{
        "description":"Discover the royal palace,its beautiful architecture,and rich history.","image":"mysuru"
    },
    "Hampi":{
        "description":"Explore ancient temples,stone monuments,and Vijayanagara Empire ruins.","image":"hampi"
    },
    "Coorg":{
        "description":"Enjoy green hills,coffee planatations,and natural scenery.","image":"coorg"
    },
    "Joy Falls":{
        "description":"Visit one of Karnataka's famous waterfalls.","image":"jog"
    },
    "Belur Temples":{
        "description":"Discover Hoysala architecture and detailed stone carvings.","image":"belur"
    }
}                

# Reusable destination display function
def show_destination(name,details):
    st.subheader(name)
    st.write(details["description"])

    image_path = find_image(details["image"])

    if image_path:
        st.image(str(image_path),caption=name,width=500)
    else:
        st.warning(
            f"Image not found:{details['image']}.jpg(or .png)."
            "Please add this photo to your images folder."
        )     
# choose a destination
st.header("Explore Karnataka")
selected_destination=st.selectbox(
    "Choose a destination",
    list(destination.keys())
)  
show_destination(selected_destination,destination[selected_destination])

st.divider()

#show all destinations
st.header("All Karnataka Destinations")

for name,details in destination.items():
    show_destination(name,details)
    st.divider()

#smart budget calculator
st.header("Smart Budget Calculator")
st.write("Enter your estimated expenses for the trip.")

transport=st.number_input(
    "Transportation cost (total ruppes)",
    min_value=0,
    value=1000,
    step=100
)  
hotel=st.number_input(
    "Hotal cost per day",
    min_value=0,
    value=1000,
    step=100
)  
food=st.number_input(
    "Food cost per day",
    min_value=0,
    value=500,
    step=100
)
activities=st.number_input(
    "sightseeing and activities (total ruppes)",
    min_value=0,
    value=500,
    step=100
)
total_cost=transport+(hotel*days)+(food*days)+activities 
remaining_budget=budget-total_cost
st.subheader("Your Trip Budget")
st.write(f"Transportation:{transport:,}")
st.write(f"Hotal:{hotel * days:,}")
st.write(f"Food:{food * days:,}")
st.write(f"Activities:{activities:,}")
st.subheader(f"Total Estimated Cost:{total_cost:,}")
if remaining_budget >=0:
    st.success("Great! Your estimated trip is within your budget:")
    st.write(f"Remaining budget:{remaining_budget:,}")
else:
    st.error(
        f"Your trip exceeds your budget by {abs(remaining_budget):,}"
        "Try reducing expenses."
    )    
