
#
#pip install pandas

subprocess.check_call([sys.executable, "-m", "pip", "install", 'catboost'])
# noinspection PyUnresolvedReferences
from catboost import CatBoostClassifier

import streamlit as st
# noinspection PyUnresolvedReferences

import pickle as pkl

st.title('In Vehicel Coupon Recommandation')
st.text('This is a web app tells whether the driver will accept the coupon or not based upon various factors')


#selection options
destination_list = ["No Urgent Place"  ,"Home" ,"Work"]

passanger_list = ['Alone' ,'Friend(s)' ,'Kid(s)' ,'Partner']
weather_list = ['Sunny', 'Rainy' ,'Snowy']
temperature_list = [55, 80 ,30]
time_list = ['2PM' ,'10AM' ,'6PM', '7AM' ,'10PM']
coupon_list = ['Restaurant(<20)' ,'Coffee House' ,'Carry out & Take away', 'Bar','Restaurant(20-50)']
expiration_list = ['1d' ,'2h']
gender_list = ['Female' ,'Male']
age_list = ['21', '46', '26' ,'31', '41' ,'50plus' ,'36' ,'below21']
maritalStatus_list = ['Unmarried partner' ,'Single' ,'Married partner' ,'Divorced' ,'Widowed']
has_children_list = [1 ,0]

education_list = ['Some college - no degree', 'Bachelors degree' ,'Associates degree','High School Graduate',\
                  'Graduate degree (Masters or Doctorate)','Some High School']
occupation_list = ['Unemployed' ,'Architecture & Engineering' ,'Student','Education&Training&Library' ,\
                   'Healthcare Support','Healthcare Practitioners & Technical' ,'Sales & Related' ,'Management',\
                     'Arts Design Selecttainment Sports & Media' ,'Computer & Mathematical',\
                   'Life Physical Social Science' ,'Personal Care & Service','Community & Social Services',\
                   'Office & Administrative Support','Construction & Extraction', 'Legal' ,'Retired',\
                     'Installation Maintenance & Repair' ,'Transportation & Material Moving','Business & Financial',\
                   'Protective Service','Food Preparation & Serving Related' ,'Production Occupations',\
                     'Building & Grounds Cleaning & Maintenance' ,'Farming Fishing & Forestry']
income_list = ['$37500 - $49999', '$62500 - $74999' ,'$12500 - $24999' ,'$75000 - $87499','$50000 - $62499' ,\
               '$25000 - $37499' ,'$100000 or More' ,'$87500 - $99999','Less than $12500']
car_list = ['nan' ,'Scooter and motorcycle' ,'crossover' ,'Mazda5' ,'do not drive'\
             ,'Car that is too old to install Onstar :D']
visits_list = ['never','less1','1~3','4~8','gt8', 'nan']
Bar_list = ['never', 'less1' ,'1~3' ,'gt8', 'nan' ,'4~8']
CoffeeHouse_list = ['never', 'less1' ,'4~8' ,'1~3' ,'gt8', 'nan']
CarryAway_list = ['nan' ,'4~8' ,'1~3', 'gt8' ,'less1' ,'never']
RestaurantLessThan20_list = ['4~8', '1~3', 'less1', 'gt8', 'nan' ,'never']
Restaurant20To50_list = ['1~3' ,'less1', 'never' ,'gt8', '4~8', 'nan']
toCoupon_GEQ5min_list = [1]
toCoupon_GEQ15min_list = [0 ,1]
toCoupon_GEQ25min_list = [0 ,1]
direction_same_list = [0 ,1]
direction_opposite_list = [1 ,0]

user_data = []

#Selections

destination_option         = st.selectbox('1. Select user Destination',(destination_list))
user_data.append(destination_option)
passanger_option           = st.selectbox('2. Select passangeer type select alone of have no passanger',(passanger_list))
user_data.append(passanger_option)
weather_option             = st.selectbox('3. Select outside weather type',(weather_list))
user_data.append(weather_option)
temperature_option         = st.selectbox('4. Select outside temperature',(temperature_list))
user_data.append(temperature_option)
time_option                = st.selectbox('5. Select time',(time_list))
user_data.append(time_option)

st.text('NOTE:- Restaurant(<20) means avergae cost per person  is less tha 20 dollars and Restaurant(20-50) means average cost per person is between 20-50 dollars')
coupon_list                = st.selectbox('6. Select Coupon Type ',(coupon_list))
user_data.append(coupon_list)
expiration_option          = st.selectbox('7. Select Coupon Expiry time',(expiration_list))
user_data.append(expiration_option)
gender_option              = st.selectbox('8. Select User Gender',(gender_list))
user_data.append(gender_option)
age_option                 = st.selectbox('9. Select User Age',(age_list))
user_data.append(age_option)
maritalStatus_option       = st.selectbox('10. Select User Marital Status',(maritalStatus_list))
user_data.append(maritalStatus_option)
has_children_option        = st.selectbox('11. Select whether User has children Or Not. 1 if yes and 0 if none',(has_children_list))
user_data.append(has_children_option)
education_option           = st.selectbox('12. Select User Education Level',(education_list))
user_data.append(education_option)
occupation_option          = st.selectbox('13. Select User Occupation',(occupation_list))
user_data.append(occupation_option)
income_option              = st.selectbox('14. Select User Income Level',(income_list))
user_data.append(income_option)
car_option                 = st.selectbox('15. Select Users Car. Select nan if not in the options',(car_list))
user_data.append(car_option)



Bar_option                  = st.selectbox('16. Select how many times the user goes to a bar every month',(Bar_list))
user_data.append(Bar_option)
CoffeeHouse_option          = st.selectbox('17. Select how many times the user goes to a CoffeHouse every month',(CoffeeHouse_list))
user_data.append(CoffeeHouse_option)
CarryAway_option            = st.selectbox('18. Select how many times user have  take-away food every month?',(CarryAway_list))
user_data.append(CarryAway_option)
RestaurantLessThan20_option = st.selectbox('19. Select  how many times the user goes to a restaurant with an average expense per person \
                                    of less than $20 every month',(RestaurantLessThan20_list))
user_data.append(RestaurantLessThan20_option)
Restaurant20To50_option    = st.selectbox('20. Select  how many times the user goes to a restaurant with an average expense per person \
                                    of less than $20 to 50 Dollars every month',(Restaurant20To50_list))
user_data.append(Restaurant20To50_option)

user_data.append(1) # appending 1 for driving time for coupon as there is only one option
toCoupon_GEQ15min_option  = st.selectbox('22. Select is the driving distance to the restaurant/bar for using the coupon is greater than 15 \
                                minutes. 1 if yes or 0 if no',(toCoupon_GEQ15min_list))
user_data.append(toCoupon_GEQ15min_option)
toCoupon_GEQ25min_option  = st.selectbox('23. Select  is the driving distance to the restaurant/bar for using the coupon is greater than 25 \
                                minutes. 1 if yes or 0 if no',(toCoupon_GEQ25min_list))
user_data.append(toCoupon_GEQ25min_option)
direction_same_option = st.selectbox('24. Select whether the restaurant/bar is in the same direction as the users current destination . 1 if yes or 0 if no'\
                                     ,(direction_same_list))
user_data.append(direction_same_option)
direction_opposite_option = st.selectbox('24. Select whether the restaurant/bar is in the opposite direction as the users current destination. 1 if yes or 0 if no'\
                                     ,(direction_opposite_list))
user_data.append(direction_opposite_option)


#Customisation functions
# https://levelup.gitconnected.com/how-to-add-a-background-image-to-your-streamlit-app-96001e0377b2
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{

             background-image: url('https://i.gifer.com/1pX9.gif');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
add_bg_from_url()
def add_bg_from_url_yes():
    '''Funtion for changing backgroun if prediction is yes'''
    st.markdown(
        f"""
         <style>
         .stApp {{

             background-image: url('https://media.giphy.com/media/3o6UB3VhArvomJHtdK/giphy.gif');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
def add_bg_from_url_no():
    '''Funtion for changing background if prediction is no'''
    st.markdown(
        f"""
         <style>
         .stApp {{

             background-image: url('https://media.giphy.com/media/MqnSnuOaYVyIDRGnis/giphy.gif');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )



#loading model
model = pkl.load(open('catboost_pkl', 'rb'))

#Functions for predictions
def pre_processing(datapoints):
    datapoints.pop(23)  # removing 'direction same'
    datapoints.pop(14)  # removing car

    most_freq_values = {'destination': 'No Urgent Place', 'passanger': 'Alone', 'weather': 'Sunny', 'temperature': 80,
                        'time': '6PM', 'coupon': 'Coffee House', 'expiration': '1d', 'gender': 'Female', 'age': '21',
                        'maritalStatus': 'Married partner',
                        'has_children': 0, 'education': 'Some college - no degree', 'occupation': 'Unemployed',
                        'income': '$25000 - $37499',
                        'Bar': 'never', 'CoffeeHouse': 'less1', 'CarryAway': '1~3',
                        'RestaurantLessThan20': '1~3', 'Restaurant20To50': '1~3', 'toCoupon_GEQ5min': 1,
                        'toCoupon_GEQ15min': 1,
                        'toCoupon_GEQ25min': 0, 'direction_opp': 1}

    for index, point in enumerate(datapoints):

        if point == 'NaN' or point == 'nan' or point == ' ':
            datapoints[index] = most_freq_values[list(most_freq_values.keys())[index]]  # filling the missing value
    return datapoints
def pipeline(datapoints):
    yes = 1
    no = 0
    datapoints = pre_processing(datapoints)
    y_pred = model.predict(datapoints)
    if y_pred == 1:
        return yes
    else:
        return no

if st.button('Click me to know the result'):
    result = pipeline(user_data)
    if result == 1:
        st.write("YES....The user will accept the coupon")
        add_bg_from_url_yes()
        st.image('https://media.giphy.com/media/dYZuqJLDVsWMLWyIxJ/giphy.gif')
    else:
        add_bg_from_url_no()
        st.write("The user will not be accepting  the coupon")
        st.image('https://media.giphy.com/media/l0HU5HuHIMVHvCYTu/giphy.gif')
