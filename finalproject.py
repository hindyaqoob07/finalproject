import tkinter as tk #This line imports the tkinter library and assigns it an alias 'tk' for easier reference.
from tkinter import messagebox # # This line imports the messagebox module from the tkinter library (to create message boxes)
import pickle


class Employee: #This line defines a class named Employee
    def __init__(self, employee_id, first_name, last_name, department, job_title, basic_salary, age, gender,
                 date_of_birth, nationality, years_of_experience, phone_number, email): # The constructor method initializes the object with the provided values for its attributes
        self.employee_id = employee_id # This line sets the employee_id attribute of the Employee object to the value passed as the employee_id parameter
        self.first_name = first_name  # This line sets the first_name attribute of the Employee object to the value passed as the first_name parameter
        self.last_name = last_name # This line sets the last_name attribute of the Employee object to the value passed as the last_name parameter
        self.department = department # This line sets the department attribute of the Employee object to the value passed as the department parameter
        self.job_title = job_title # This line sets the job_title attribute of the Employee object to the value passed as the job_title parameter
        self.basic_salary = basic_salary # This line sets the basic_salary attribute of the Employee object to the value passed as the basic_salary parameter
        self.age = age # This line sets the age attribute of the Employee object to the value passed as the age parameter
        self.gender = gender # This line sets the gender attribute of the Employee object to the value passed as the gender parameter
        self.date_of_birth = date_of_birth # This line sets the date_of_birth attribute of the Employee object to the value passed as the date_of_birth parameter
        self.nationality = nationality # This line sets the nationality attribute of the Employee object to the value passed as the nationality parameter
        self.years_of_experience = years_of_experience # This line sets the years_of_experience attribute of the Employee object to the value passed as the years_of_experience parameter
        self.phone_number = phone_number # This line sets the phone_number attribute of the Employee object to the value passed as the phone_number parameter
        self.email = email # This line sets the email attribute of the Employee object to the value passed as the email parameter
class Client: #This line defines a class named Client
    def __init__(self, client_id, first_name, last_name, gender, number, email, num_of_guests, budget, event_type, address, event_preference, event_history, communication_method, event_date_flexibility, event_theme_preferences, special_requests, referral_source, follow_up_history, event_timeline): # The constructor method initializes the object with the provided values for its attributes
        self.client_id = client_id # This line sets the client_id attribute of the Client object to the value passed as the client_id parameter
        self.first_name = first_name # This line sets the first_name attribute of the Client object to the value passed as the first_name parameter
        self.last_name = last_name # This line sets the last_name attribute of the Client object to the value passed as the last_name parameter
        self.gender = gender # This line sets the gender attribute of the Client object to the value passed as the gender parameter
        self.number = number # This line sets the number attribute of the Client object to the value passed as the number parameter
        self.email = email # This line sets the email attribute of the Client object to the value passed as the email parameter
        self.num_of_guests = num_of_guests # This line sets the num_of_guests attribute of the Client object to the value passed as the num_of_guests parameter
        self.budget = budget # This line sets the budget attribute of the Client object to the value passed as the budget parameter
        self.event_type = event_type # This line sets the event_type attribute of the Client object to the value passed as the event_type parameter
        self.address = address # This line sets the address attribute of the Client object to the value passed as the address parameter
        self.event_preference = event_preference # This line sets the event_preference attribute of the Client object to the value passed as the event_preference parameter
        self.event_history = event_history # This line sets the event_history attribute of the Client object to the value passed as the event_history parameter
        self.communication_method = communication_method # This line sets the communication_method attribute of the Client object to the value passed as the communication_method parameter
        self.event_date_flexibility = event_date_flexibility # This line sets the event_date_flexibility attribute of the Client object to the value passed as the event_date_flexibility parameter
        self.event_theme_preferences = event_theme_preferences # This line sets the event_theme_preferences attribute of the Client object to the value passed as the event_theme_preferences parameter
        self.special_requests = special_requests # This line sets the special_requests attribute of the Client object to the value passed as the special_requests parameter
        self.referral_source = referral_source # This line sets the referral_source attribute of the Client object to the value passed as the referral_source parameter
        self.follow_up_history = follow_up_history # This line sets the follow_up_history attribute of the Client object to the value passed as the follow_up_history parameter
        self.event_timeline = event_timeline # This line sets the event_timeline attribute of the Client object to the value passed as the event_timeline parameter
class Supplier: #This line defines a class named Supplier
    def __init__(self, ID, name, email, phone_number, pricing, credit_terms, payment_terms,
                 shipping, specialization, service_area, availability, quality_assurance,
                 ratings_reviews, preferred_communication_method, contract_details,
                 feedback_history, payment_history): # The constructor method initializes the object with the provided values for its attributes
        self.ID = ID # This line sets the ID attribute of the Supplier object to the value passed as the ID parameter
        self.name = name # This line sets the name attribute of the Supplier object to the value passed as the name parameter
        self.email = email # This line sets the email attribute of the Supplier object to the value passed as the email parameter
        self.phone_number = phone_number # This line sets the phone_number attribute of the Supplier object to the value passed as the phone_number parameter
        self.pricing = pricing # This line sets the pricing attribute of the Supplier object to the value passed as the pricing parameter
        self.credit_terms = credit_terms # This line sets the credit_terms attribute of the Supplier object to the value passed as the credit_terms parameter
        self.payment_terms = payment_terms # This line sets the payment_terms attribute of the Supplier object to the value passed as the payment_terms parameter
        self.shipping = shipping # This line sets the shipping attribute of the Supplier object to the value passed as the shipping parameter
        self.specialization = specialization # This line sets the specialization attribute of the Supplier object to the value passed as the specialization parameter
        self.service_area = service_area # This line sets the service_area attribute of the Supplier object to the value passed as the service_area parameter
        self.availability = availability # This line sets the availability attribute of the Supplier object to the value passed as the availability parameter
        self.quality_assurance = quality_assurance # This line sets the quality_assurance attribute of the Supplier object to the value passed as the quality_assurance parameter
        self.ratings_reviews = ratings_reviews # This line sets the ratings_reviews attribute of the Supplier object to the value passed as the ratings_reviews parameter
        self.preferred_communication_method = preferred_communication_method # This line sets the preferred_communication_method attribute of the Supplier object to the value passed as the preferred_communication_method parameter
        self.contract_details = contract_details # This line sets the contract_details attribute of the Supplier object to the value passed as the contract_details parameter
        self.feedback_history = feedback_history # This line sets the feedback_history attribute of the Supplier object to the value passed as the feedback_history parameter
        self.payment_history = payment_history # This line sets the payment_history attribute of the Supplier object to the value passed as the payment_history parameter
class Event: #This line defines a class named Event
    def __init__(self, event_ID, date, time, title, type_of_event, address, duration, guest_list, catering_company,
                 cleaning_company, decorations_company, venue, theme, num_of_guests, min_of_guests, music, giveaways,
                 entertainment_company, furniture_supply_company, invoice, event_budget, event_marketing_materials,
                 event_sponsorships): # The constructor method initializes the object with the provided values for its attributes
        self.event_ID = event_ID # This line sets the event_ID attribute of the Event object to the value passed as the event_ID parameter
        self.date = date # This line sets the date attribute of the Event object to the value passed as the date parameter
        self.time = time # This line sets the time attribute of the Event object to the value passed as the time parameter
        self.title = title # This line sets the title attribute of the Event object to the value passed as the title parameter
        self.type_of_event = type_of_event # This line sets the type_of_event attribute of the Event object to the value passed as the type_of_event parameter
        self.address = address # This line sets the address attribute of the Event object to the value passed as the address parameter
        self.duration = duration # This line sets the duration attribute of the Event object to the value passed as the duration parameter
        self.guest_list = guest_list # This line sets the guest_list attribute of the Event object to the value passed as the guest_list parameter
        self.catering_company = catering_company # This line sets the catering_company attribute of the Event object to the value passed as the catering_company parameter
        self.cleaning_company = cleaning_company # This line sets the cleaning_company attribute of the Event object to the value passed as the cleaning_company parameter
        self.decorations_company = decorations_company # This line sets the decorations_company attribute of the Event object to the value passed as the decorations_company parameter
        self.venue = venue # This line sets the venue attribute of the Event object to the value passed as the venue parameter
        self.theme = theme # This line sets the theme attribute of the Event object to the value passed as the theme parameter
        self.num_of_guests = num_of_guests # This line sets the num_of_guests attribute of the Event object to the value passed as the num_of_guests parameter
        self.min_of_guests = min_of_guests # This line sets the min_of_guests attribute of the Event object to the value passed as the min_of_guests parameter
        self.music = music # This line sets the music attribute of the Event object to the value passed as the music parameter
        self.giveaways = giveaways # This line sets the giveaways attribute of the Event object to the value passed as the giveaways parameter
        self.entertainment_company = entertainment_company # This line sets the entertainment_company attribute of the Event object to the value passed as the entertainment_company parameter
        self.furniture_supply_company = furniture_supply_company # This line sets the furniture_supply_company attribute of the Event object to the value passed as the furniture_supply_company parameter
        self.invoice = invoice # This line sets the invoice attribute of the Event object to the value passed as the invoice parameter
        self.event_budget = event_budget # This line sets the event_budget attribute of the Event object to the value passed as the event_budget parameter
        self.event_marketing_materials = event_marketing_materials # This line sets the event_marketing_materials attribute of the Event object to the value passed as the event_marketing_materials parameter
        self.event_sponsorships = event_sponsorships # This line sets the event_sponsorships attribute of the Event object to the value passed as the event_sponsorships parameter

class Venue: #This line defines a class named Venue
    def __init__(self, venue_ID, name, address, contact, min_guests, max_guests, price, dress_code, amenities, availability_calendar, capacity, photos, layout): # The constructor method initializes the object with the provided values for its attributes
        self.venue_ID = venue_ID # This line sets the venue_ID attribute of the Venue object to the value passed as the venue_ID parameter
        self.name = name # This line sets the name attribute of the Venue object to the value passed as the name parameter
        self.address = address # This line sets the address attribute of the Venue object to the value passed as the address parameter
        self.contact = contact # This line sets the contact attribute of the Venue object to the value passed as the contact parameter
        self.min_guests = min_guests # This line sets the min_guests attribute of the Venue object to the value passed as the min_guests parameter
        self.max_guests = max_guests # This line sets the max_guests attribute of the Venue object to the value passed as the max_guests parameter
        self.price = price # This line sets the price attribute of the Venue object to the value passed as the price parameter
        self.dress_code = dress_code # This line sets the dress_code attribute of the Venue object to the value passed as the dress_code parameter
        self.amenities = amenities # This line sets the amenities attribute of the Venue object to the value passed as the amenities parameter
        self.availability_calendar = availability_calendar # This line sets the availability_calendar attribute of the Venue object to the value passed as the availability_calendar parameter
        self.capacity = capacity # This line sets the capacity attribute of the Venue object to the value passed as the capacity parameter
        self.photos = photos # This line sets the photos attribute of the Venue object to the value passed as the photos parameter
        self.layout = layout # This line sets the layout attribute of the Venue object to the value passed as the layout parameter

class CateringCompany: #This lCateringCompanyine defines a class named CateringCompany
    def __init__(self, caterer_ID, name, address, phone_number, email, instagram, facebook, menu, min_guests, max_guests, price, client_ID, event_ID, catering_equipment, service_level, setup_requirements): # The constructor method initializes the object with the provided values for its attributes
        self.caterer_ID = caterer_ID # This line sets the caterer_ID attribute of the CateringCompany object to the value passed as the caterer_ID parameter
        self.name = name # This line sets the name attribute of the CateringCompany object to the value passed as the name parameter
        self.address = address # This line sets the address attribute of the CateringCompany object to the value passed as the address parameter
        self.phone_number = phone_number # This line sets the phone_number attribute of the CateringCompany object to the value passed as the phone_number parameter
        self.email = email # This line sets the email attribute of the CateringCompany object to the value passed as the email parameter
        self.instagram = instagram # This line sets the instagram attribute of the CateringCompany object to the value passed as the instagram parameter
        self.facebook = facebook # This line sets the facebook attribute of the CateringCompany object to the value passed as the facebook parameter
        self.menu = menu # This line sets the menu attribute of the CateringCompany object to the value passed as the menu parameter
        self.min_guests = min_guests # This line sets the min_guests attribute of the CateringCompany object to the value passed as the min_guests parameter
        self.max_guests = max_guests # This line sets the max_guests attribute of the CateringCompany object to the value passed as the max_guests parameter
        self.price = price # This line sets the price attribute of the CateringCompany object to the value passed as the price parameter
        self.client_ID = client_ID # This line sets the client_ID attribute of the CateringCompany object to the value passed as the client_ID parameter
        self.event_ID = event_ID # This line sets the event_ID attribute of the CateringCompany object to the value passed as the event_ID parameter
        self.catering_equipment = catering_equipment # This line sets the catering_equipment attribute of the CateringCompany object to the value passed as the catering_equipment parameter
        self.service_level = service_level # This line sets the service_level attribute of the CateringCompany object to the value passed as the service_level parameter
        self.setup_requirements = setup_requirements # This line sets the setup_requirements attribute of the CateringCompany object to the value passed as the setup_requirements parameter

class EventManagementsystem: #This line defines a class named EventManagementsystem
    def __init__(self, root): # The constructor method initializes the object with the provided values for its attributes
        self.suppliers_text = None #This line initializes suppliers_text attribute to None
        self.root = root #This line assigns the passed root parameter to the object's root attribute
        self.root.title("Event Management System :") # This line sets the title of the root window to "Event Management System :"

        # From here up to line 439, the lines create labels and entry widgets for each attribute of each class
        self.employee_id_label = tk.Label(root, text="Employee ID:")
        self.employee_id_entry = tk.Entry(root)

        self.first_name_label = tk.Label(root, text="First Name:")
        self.first_name_entry = tk.Entry(root)

        self.last_name_label = tk.Label(root, text="Last Name:")
        self.last_name_entry = tk.Entry(root)

        self.department_label = tk.Label(root, text="Department:")
        self.department_entry = tk.Entry(root)

        self.job_title_label = tk.Label(root, text="Job Title:")
        self.job_title_entry = tk.Entry(root)

        self.basic_salary_label = tk.Label(root, text="Basic Salary:")
        self.basic_salary_entry = tk.Entry(root)

        self.age_label = tk.Label(root, text="Age:")
        self.age_entry = tk.Entry(root)

        self.gender_label = tk.Label(root, text="Gender:")
        self.gender_entry = tk.Entry(root)

        self.date_of_birth_label = tk.Label(root, text="Date of Birth:")
        self.date_of_birth_entry = tk.Entry(root)

        self.nationality_label = tk.Label(root, text="Nationality:")
        self.nationality_entry = tk.Entry(root)

        self.years_of_experience_label = tk.Label(root, text="Years of Experience:")
        self.years_of_experience_entry = tk.Entry(root)

        self.phone_number_label = tk.Label(root, text="Phone Number:")
        self.phone_number_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.client_id_label = tk.Label(root, text="Client ID:")
        self.client_id_entry = tk.Entry(root)

        self.client_first_name_label = tk.Label(root, text="First Name:")
        self.client_first_name_entry = tk.Entry(root)

        self.client_last_name_label = tk.Label(root, text="Last Name:")
        self.client_last_name_entry = tk.Entry(root)

        self.client_gender_label = tk.Label(root, text="Gender:")
        self.client_gender_entry = tk.Entry(root)

        self.client_number_label = tk.Label(root, text="Number:")
        self.client_number_entry = tk.Entry(root)

        self.client_email_label = tk.Label(root, text="Email:")
        self.client_email_entry = tk.Entry(root)

        self.client_num_of_guests_label = tk.Label(root, text="Number of Guests:")
        self.client_num_of_guests_entry = tk.Entry(root)

        self.client_budget_label = tk.Label(root, text="Budget:")
        self.client_budget_entry = tk.Entry(root)

        self.client_event_type_label = tk.Label(root, text="Type of Event:")
        self.client_event_type_entry = tk.Entry(root)

        self.client_address_label = tk.Label(root, text="Address:")
        self.client_address_entry = tk.Entry(root)

        self.client_event_preference_label = tk.Label(root, text="Event Preference:")
        self.client_event_preference_entry = tk.Entry(root)

        self.client_event_history_label = tk.Label(root, text="Event History:")
        self.client_event_history_entry = tk.Entry(root)

        self.client_communication_method_label = tk.Label(root, text="Preferred Communication Method:")
        self.client_communication_method_entry = tk.Entry(root)

        self.client_event_date_flexibility_label = tk.Label(root, text="Event Date Flexibility:")
        self.client_event_date_flexibility_entry = tk.Entry(root)

        self.client_event_theme_preferences_label = tk.Label(root, text="Event Theme Preferences:")
        self.client_event_theme_preferences_entry = tk.Entry(root)

        self.client_special_requests_label = tk.Label(root, text="Special Requests or Notes:")
        self.client_special_requests_entry = tk.Entry(root)

        self.client_referral_source_label = tk.Label(root, text="Referral Source:")
        self.client_referral_source_entry = tk.Entry(root)

        self.client_follow_up_history_label = tk.Label(root, text="Follow-up History:")
        self.client_follow_up_history_entry = tk.Entry(root)

        self.client_event_timeline_label = tk.Label(root, text="Event Timeline:")
        self.client_event_timeline_entry = tk.Entry(root)

        self.supplier_id_label = tk.Label(root, text="Supplier ID:")
        self.supplier_id_entry = tk.Entry(root)

        self.supplier_name_label = tk.Label(root, text="Name:")
        self.supplier_name_entry = tk.Entry(root)

        self.supplier_email_label = tk.Label(root, text="Email:")
        self.supplier_email_entry = tk.Entry(root)

        self.supplier_phone_number_label = tk.Label(root, text="Phone Number:")
        self.supplier_phone_number_entry = tk.Entry(root)

        self.supplier_pricing_label = tk.Label(root, text="Pricing:")
        self.supplier_pricing_entry = tk.Entry(root)

        self.supplier_credit_terms_label = tk.Label(root, text="Credit Terms:")
        self.supplier_credit_terms_entry = tk.Entry(root)

        self.supplier_payment_terms_label = tk.Label(root, text="Payment Terms:")
        self.supplier_payment_terms_entry = tk.Entry(root)

        self.supplier_shipping_label = tk.Label(root, text="Shipping:")
        self.supplier_shipping_entry = tk.Entry(root)

        self.supplier_specialization_label = tk.Label(root, text="Specialization:")
        self.supplier_specialization_entry = tk.Entry(root)

        self.supplier_service_area_label = tk.Label(root, text="Service Area:")
        self.supplier_service_area_entry = tk.Entry(root)

        self.supplier_availability_label = tk.Label(root, text="Availability:")
        self.supplier_availability_entry = tk.Entry(root)

        self.supplier_quality_assurance_label = tk.Label(root, text="Quality Assurance:")
        self.supplier_quality_assurance_entry = tk.Entry(root)

        self.supplier_ratings_reviews_label = tk.Label(root, text="Ratings/Reviews:")
        self.supplier_ratings_reviews_entry = tk.Entry(root)

        self.supplier_preferred_communication_label = tk.Label(root, text="Preferred Communication:")
        self.supplier_preferred_communication_entry = tk.Entry(root)

        self.supplier_contract_details_label = tk.Label(root, text="Contract Details:")
        self.supplier_contract_details_entry = tk.Entry(root)

        self.supplier_feedback_history_label = tk.Label(root, text="Feedback History:")
        self.supplier_feedback_history_entry = tk.Entry(root)

        self.supplier_payment_history_label = tk.Label(root, text="Payment History:")
        self.supplier_payment_history_entry = tk.Entry(root)

        self.event_id_label = tk.Label(root, text="Event ID:")
        self.event_id_entry = tk.Entry(root)

        self.date_label = tk.Label(root, text="Date:")
        self.date_entry = tk.Entry(root)

        self.time_label = tk.Label(root, text="Time:")
        self.time_entry = tk.Entry(root)

        self.title_label = tk.Label(root, text="Title:")
        self.title_entry = tk.Entry(root)

        self.type_of_event_label = tk.Label(root, text="Type of Event:")
        self.type_of_event_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.duration_label = tk.Label(root, text="Duration:")
        self.duration_entry = tk.Entry(root)

        self.guest_list_label = tk.Label(root, text="Guest List:")
        self.guest_list_entry = tk.Entry(root)

        self.catering_company_label = tk.Label(root, text="Catering Company:")
        self.catering_company_entry = tk.Entry(root)

        self.cleaning_company_label = tk.Label(root, text="Cleaning Company:")
        self.cleaning_company_entry = tk.Entry(root)

        self.decorations_company_label = tk.Label(root, text="Decorations Company:")
        self.decorations_company_entry = tk.Entry(root)

        self.venue_label = tk.Label(root, text="Venue:")
        self.venue_entry = tk.Entry(root)

        self.theme_label = tk.Label(root, text="Theme:")
        self.theme_entry = tk.Entry(root)

        self.num_of_guests_label = tk.Label(root, text="Number of Guests:")
        self.num_of_guests_entry = tk.Entry(root)

        self.min_of_guests_label = tk.Label(root, text="Min Guests:")
        self.min_of_guests_entry = tk.Entry(root)

        self.music_label = tk.Label(root, text="Music:")
        self.music_entry = tk.Entry(root)

        self.giveaways_label = tk.Label(root, text="Giveaways:")
        self.giveaways_entry = tk.Entry(root)

        self.entertainment_company_label = tk.Label(root, text="Entertainment Company:")
        self.entertainment_company_entry = tk.Entry(root)

        self.furniture_supply_company_label = tk.Label(root, text="Furniture Supply Company:")
        self.furniture_supply_company_entry = tk.Entry(root)

        self.invoice_label = tk.Label(root, text="Invoice:")
        self.invoice_entry = tk.Entry(root)

        self.event_budget_label = tk.Label(root, text="Event Budget:")
        self.event_budget_entry = tk.Entry(root)

        self.event_marketing_materials_label = tk.Label(root, text="Event Marketing Materials:")
        self.event_marketing_materials_entry = tk.Entry(root)

        self.event_sponsorships_label = tk.Label(root, text="Event Sponsorships:")
        self.event_sponsorships_entry = tk.Entry(root)

        # Venue labels and entry widgets
        self.venue_id_label = tk.Label(root, text="Venue ID:")
        self.venue_id_entry = tk.Entry(root)

        self.venue_name_label = tk.Label(root, text="Venue Name:")
        self.venue_name_entry = tk.Entry(root)

        self.venue_address_label = tk.Label(root, text="Venue Address:")
        self.venue_address_entry = tk.Entry(root)

        self.venue_contact_label = tk.Label(root, text="Venue Contact:")
        self.venue_contact_entry = tk.Entry(root)

        self.min_guests_venue_label = tk.Label(root, text="Min Guests:")
        self.min_guests_venue_entry = tk.Entry(root)

        self.max_guests_venue_label = tk.Label(root, text="Max Guests:")
        self.max_guests_venue_entry = tk.Entry(root)

        self.venue_price_label = tk.Label(root, text="Venue Price:")
        self.venue_price_entry = tk.Entry(root)

        self.venue_dress_code_label = tk.Label(root, text="Dress Code:")
        self.venue_dress_code_entry = tk.Entry(root)

        self.venue_amenities_label = tk.Label(root, text="Venue Amenities:")
        self.venue_amenities_entry = tk.Entry(root)

        self.venue_availability_label = tk.Label(root, text="Venue Availability:")
        self.venue_availability_entry = tk.Entry(root)

        self.venue_capacity_label = tk.Label(root, text="Venue Capacity:")
        self.venue_capacity_entry = tk.Entry(root)

        self.venue_photos_label = tk.Label(root, text="Venue Photos:")
        self.venue_photos_entry = tk.Entry(root)

        self.venue_layout_label = tk.Label(root, text="Venue Layout:")
        self.venue_layout_entry = tk.Entry(root)

        self.caterer_id_label = tk.Label(root, text="Caterer ID:")
        self.caterer_id_entry = tk.Entry(root)

        self.caterer_name_label = tk.Label(root, text="Caterer Name:")
        self.caterer_name_entry = tk.Entry(root)

        self.caterer_address_label = tk.Label(root, text="Caterer Address:")
        self.caterer_address_entry = tk.Entry(root)

        self.caterer_phone_label = tk.Label(root, text="Caterer Phone:")
        self.caterer_phone_entry = tk.Entry(root)

        self.caterer_email_label = tk.Label(root, text="Caterer Email:")
        self.caterer_email_entry = tk.Entry(root)

        self.caterer_instagram_label = tk.Label(root, text="Caterer Instagram:")
        self.caterer_instagram_entry = tk.Entry(root)

        self.caterer_facebook_label = tk.Label(root, text="Caterer Facebook:")
        self.caterer_facebook_entry = tk.Entry(root)

        self.caterer_menu_label = tk.Label(root, text="Caterer Menu:")
        self.caterer_menu_entry = tk.Entry(root)

        self.caterer_min_guests_label = tk.Label(root, text="Min Guests:")
        self.caterer_min_guests_entry = tk.Entry(root)

        self.caterer_max_guests_label = tk.Label(root, text="Max Guests:")
        self.caterer_max_guests_entry = tk.Entry(root)

        self.caterer_price_label = tk.Label(root, text="Caterer Price:")
        self.caterer_price_entry = tk.Entry(root)

        self.caterer_client_id_label = tk.Label(root, text="Client ID:")
        self.caterer_client_id_entry = tk.Entry(root)

        self.caterer_event_id_label = tk.Label(root, text="Event ID:")
        self.caterer_event_id_entry = tk.Entry(root)

        self.caterer_equipment_label = tk.Label(root, text="Caterer Equipment:")
        self.caterer_equipment_entry = tk.Entry(root)

        self.caterer_service_level_label = tk.Label(root, text="Service Level:")
        self.caterer_service_level_entry = tk.Entry(root)

        self.caterer_setup_requirements_label = tk.Label(root, text="Setup Requirements:")
        self.caterer_setup_requirements_entry = tk.Entry(root)

        # These lines create buttons for Employee class
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.delete_button = tk.Button(root, text="Delete Employee", command=self.delete_employee)
        self.modify_button = tk.Button(root, text="Modify Employee", command=self.modify_employee)
        self.display_button = tk.Button(root, text="Display Employees", command=self.display_employees)
        self.display_single_button = tk.Button(root, text="Display Single Employee",
                                               command=self.display_single_employee)
        # These lines create buttons for Client class
        self.add_client_button = tk.Button(root, text="Add Client", command=self.add_client)
        self.delete_client_button = tk.Button(root, text="Delete Client", command=self.delete_client)
        self.modify_client_button = tk.Button(root, text="Modify Client", command=self.modify_client)
        self.display_clients_button = tk.Button(root, text="Display Clients", command=self.display_clients)
        self.display_single_client_button = tk.Button(root, text="Display Single Client",

                                                      command=self.display_single_client)
        # These lines create buttons for Supplier class
        self.add_supplier_button = tk.Button(root, text="Add Supplier", command=self.add_supplier)
        self.delete_supplier_button = tk.Button(root, text="Delete Supplier", command=self.delete_supplier)
        self.modify_supplier_button = tk.Button(root, text="Modify Supplier", command=self.modify_supplier)
        self.display_suppliers_button = tk.Button(root, text="Display Suppliers", command=self.display_suppliers)
        self.display_single_supplier_button = tk.Button(root, text="Display Single Supplier",command=self.display_single_supplier)

        # These lines create buttons for Event class
        self.add_event_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.delete_event_button = tk.Button(root, text="Delete Event", command=self.delete_event)
        self.modify_event_button = tk.Button(root, text="Modify Event", command=self.modify_event)
        self.display_events_button = tk.Button(root, text="Display Events", command=self.display_events)
        self.display_single_event_button = tk.Button(root, text="Display Single Event",command=self.display_single_event)

        # These lines create buttons for Venue class
        self.add_venue_button = tk.Button(root, text="Add Venue", command=self.add_venue)
        self.delete_venue_button = tk.Button(root, text="Delete Venue", command=self.delete_venue)
        self.modify_venue_button = tk.Button(root, text="Modify Venue", command=self.modify_venue)
        self.display_venues_button = tk.Button(root, text="Display Venues", command=self.display_venues)
        self.display_single_venue_button = tk.Button(root, text="Display Single Venue",command=self.display_single_venue)

        # These lines create buttons for CateringCompany class
        self.add_catering_button = tk.Button(root, text="Add Catering", command=self.add_caterer)
        self.delete_catering_button = tk.Button(root, text="Delete Catering", command=self.delete_caterer)
        self.modify_catering_button = tk.Button(root, text="Modify Catering", command=self.modify_caterer)
        self.display_catering_button = tk.Button(root, text="Display Catering", command=self.display_caterers)
        self.display_single_catering_button = tk.Button(root, text="Display Single Catering",command=self.display_single_catering)

        # (from here until line 776): Place Employee, Client, Supplier, Event, Venue and cateringcompany widgets on the grid
        self.employee_id_label.grid(row=0, column=0)
        self.employee_id_entry.grid(row=0, column=1)

        self.first_name_label.grid(row=1, column=0)
        self.first_name_entry.grid(row=1, column=1)

        self.last_name_label.grid(row=2, column=0)
        self.last_name_entry.grid(row=2, column=1)

        self.department_label.grid(row=3, column=0)
        self.department_entry.grid(row=3, column=1)

        self.job_title_label.grid(row=4, column=0)
        self.job_title_entry.grid(row=4, column=1)

        self.basic_salary_label.grid(row=5, column=0)
        self.basic_salary_entry.grid(row=5, column=1)

        self.age_label.grid(row=6, column=0)
        self.age_entry.grid(row=6, column=1)

        self.gender_label.grid(row=7, column=0)
        self.gender_entry.grid(row=7, column=1)

        self.date_of_birth_label.grid(row=8, column=0)
        self.date_of_birth_entry.grid(row=8, column=1)

        self.nationality_label.grid(row=9, column=0)
        self.nationality_entry.grid(row=9, column=1)

        self.years_of_experience_label.grid(row=10, column=0)
        self.years_of_experience_entry.grid(row=10, column=1)

        self.phone_number_label.grid(row=11, column=0)
        self.phone_number_entry.grid(row=11, column=1)

        self.email_label.grid(row=12, column=0)
        self.email_entry.grid(row=12, column=1)

        self.add_button.grid(row=13, column=0)
        self.delete_button.grid(row=13, column=1)
        self.modify_button.grid(row=14, column=0)
        self.display_button.grid(row=14, column=1)
        self.display_single_button.grid(row=15, column=0, columnspan=2)

        self.client_id_label.grid(row=0, column=2)
        self.client_id_entry.grid(row=0, column=3)

        self.client_first_name_label.grid(row=1, column=2)
        self.client_first_name_entry.grid(row=1, column=3)

        self.client_last_name_label.grid(row=2, column=2)
        self.client_last_name_entry.grid(row=2, column=3)

        self.client_gender_label.grid(row=3, column=2)
        self.client_gender_entry.grid(row=3, column=3)

        self.client_number_label.grid(row=4, column=2)
        self.client_number_entry.grid(row=4, column=3)

        self.client_email_label.grid(row=5, column=2)
        self.client_email_entry.grid(row=5, column=3)

        self.client_num_of_guests_label.grid(row=6, column=2)
        self.client_num_of_guests_entry.grid(row=6, column=3)

        self.client_budget_label.grid(row=7, column=2)
        self.client_budget_entry.grid(row=7, column=3)

        self.client_event_type_label.grid(row=8, column=2)
        self.client_event_type_entry.grid(row=8, column=3)

        self.client_address_label.grid(row=9, column=2)
        self.client_address_entry.grid(row=9, column=3)

        self.client_event_preference_label.grid(row=10, column=2)
        self.client_event_preference_entry.grid(row=10, column=3)

        self.client_event_history_label.grid(row=11, column=2)
        self.client_event_history_entry.grid(row=11, column=3)

        self.client_communication_method_label.grid(row=12, column=2)
        self.client_communication_method_entry.grid(row=12, column=3)

        self.client_event_date_flexibility_label.grid(row=13, column=2)
        self.client_event_date_flexibility_entry.grid(row=13, column=3)

        self.client_event_theme_preferences_label.grid(row=14, column=2)
        self.client_event_theme_preferences_entry.grid(row=14, column=3)

        self.client_special_requests_label.grid(row=15, column=2)
        self.client_special_requests_entry.grid(row=15, column=3)

        self.client_referral_source_label.grid(row=16, column=2)
        self.client_referral_source_entry.grid(row=16, column=3)

        self.client_follow_up_history_label.grid(row=17, column=2)
        self.client_follow_up_history_entry.grid(row=17, column=3)

        self.client_event_timeline_label.grid(row=18, column=2)
        self.client_event_timeline_entry.grid(row=18, column=3)

        row_offset = 16
        row_offset = 0  # This line starts at the same row as the client widgets

        self.supplier_id_label.grid(row=row_offset, column=4)
        self.supplier_id_entry.grid(row=row_offset, column=5)

        self.supplier_name_label.grid(row=row_offset + 1, column=4)
        self.supplier_name_entry.grid(row=row_offset + 1, column=5)

        self.supplier_email_label.grid(row=row_offset + 2, column=4)
        self.supplier_email_entry.grid(row=row_offset + 2, column=5)

        self.supplier_phone_number_label.grid(row=row_offset + 3, column=4)
        self.supplier_phone_number_entry.grid(row=row_offset + 3, column=5)

        self.supplier_pricing_label.grid(row=row_offset + 4, column=4)
        self.supplier_pricing_entry.grid(row=row_offset + 4, column=5)

        self.supplier_credit_terms_label.grid(row=row_offset + 5, column=4)
        self.supplier_credit_terms_entry.grid(row=row_offset + 5, column=5)

        self.supplier_payment_terms_label.grid(row=row_offset + 6, column=4)
        self.supplier_payment_terms_entry.grid(row=row_offset + 6, column=5)

        self.supplier_shipping_label.grid(row=row_offset + 7, column=4)
        self.supplier_shipping_entry.grid(row=row_offset + 7, column=5)

        self.supplier_specialization_label.grid(row=row_offset + 8, column=4)
        self.supplier_specialization_entry.grid(row=row_offset + 8, column=5)

        self.supplier_service_area_label.grid(row=row_offset + 9, column=4)
        self.supplier_service_area_entry.grid(row=row_offset + 9, column=5)

        self.supplier_availability_label.grid(row=row_offset + 10, column=4)
        self.supplier_availability_entry.grid(row=row_offset + 10, column=5)

        self.supplier_quality_assurance_label.grid(row=row_offset + 11, column=4)
        self.supplier_quality_assurance_entry.grid(row=row_offset + 11, column=5)

        self.supplier_ratings_reviews_label.grid(row=row_offset + 12, column=4)
        self.supplier_ratings_reviews_entry.grid(row=row_offset + 12, column=5)

        self.supplier_preferred_communication_label.grid(row=row_offset + 13, column=4)
        self.supplier_preferred_communication_entry.grid(row=row_offset + 13, column=5)

        self.supplier_contract_details_label.grid(row=row_offset + 14, column=4)
        self.supplier_contract_details_entry.grid(row=row_offset + 14, column=5)

        self.supplier_feedback_history_label.grid(row=row_offset + 15, column=4)
        self.supplier_feedback_history_entry.grid(row=row_offset + 15, column=5)

        self.supplier_payment_history_label.grid(row=row_offset + 16, column=4)
        self.supplier_payment_history_entry.grid(row=row_offset + 16, column=5)

        self.event_id_label.grid(row=row_offset, column=6)
        self.event_id_entry.grid(row=row_offset, column=7)

        self.date_label.grid(row=row_offset + 1, column=6)
        self.date_entry.grid(row=row_offset + 1, column=7)

        self.time_label.grid(row=row_offset + 2, column=6)
        self.time_entry.grid(row=row_offset + 2, column=7)

        self.title_label.grid(row=row_offset + 3, column=6)
        self.title_entry.grid(row=row_offset + 3, column=7)

        self.type_of_event_label.grid(row=row_offset + 4, column=6)
        self.type_of_event_entry.grid(row=row_offset + 4, column=7)

        self.address_label.grid(row=row_offset + 5, column=6)
        self.address_entry.grid(row=row_offset + 5, column=7)

        self.duration_label.grid(row=row_offset + 6, column=6)
        self.duration_entry.grid(row=row_offset + 6, column=7)

        self.guest_list_label.grid(row=row_offset + 7, column=6)
        self.guest_list_entry.grid(row=row_offset + 7, column=7)

        self.catering_company_label.grid(row=row_offset + 8, column=6)
        self.catering_company_entry.grid(row=row_offset + 8, column=7)

        self.cleaning_company_label.grid(row=row_offset + 9, column=6)
        self.cleaning_company_entry.grid(row=row_offset + 9, column=7)

        self.decorations_company_label.grid(row=row_offset + 10, column=6)
        self.decorations_company_entry.grid(row=row_offset + 10, column=7)

        self.venue_label.grid(row=row_offset + 11, column=6)
        self.venue_entry.grid(row=row_offset + 11, column=7)

        self.theme_label.grid(row=row_offset + 12, column=6)
        self.theme_entry.grid(row=row_offset + 12, column=7)

        self.num_of_guests_label.grid(row=row_offset + 13, column=6)
        self.num_of_guests_entry.grid(row=row_offset + 13, column=7)


        self.music_label.grid(row=row_offset + 14, column=6)
        self.music_entry.grid(row=row_offset + 14, column=7)

        self.giveaways_label.grid(row=row_offset + 15, column=6)
        self.giveaways_entry.grid(row=row_offset + 15, column=7)

        self.entertainment_company_label.grid(row=row_offset + 16, column=6)
        self.entertainment_company_entry.grid(row=row_offset + 16, column=7)

        self.furniture_supply_company_label.grid(row=row_offset + 17, column=6)
        self.furniture_supply_company_entry.grid(row=row_offset + 17, column=7)

        self.invoice_label.grid(row=row_offset + 18, column=6)
        self.invoice_entry.grid(row=row_offset + 18, column=7)

        self.event_budget_label.grid(row=row_offset + 19, column=6)
        self.event_budget_entry.grid(row=row_offset + 19, column=7)

        self.event_sponsorships_label.grid(row=row_offset + 20, column=6)
        self.event_sponsorships_entry.grid(row=row_offset + 20, column=7)

        self.venue_id_label.grid(row=row_offset, column=8)
        self.venue_id_entry.grid(row=row_offset, column=9)

        self.venue_name_label.grid(row=row_offset + 1, column=8)
        self.venue_name_entry.grid(row=row_offset + 1, column=9)

        self.venue_address_label.grid(row=row_offset + 2, column=8)
        self.venue_address_entry.grid(row=row_offset + 2, column=9)

        self.venue_contact_label.grid(row=row_offset + 3, column=8)
        self.venue_contact_entry.grid(row=row_offset + 3, column=9)

        self.min_guests_venue_label.grid(row=row_offset + 4, column=8)
        self.min_guests_venue_entry.grid(row=row_offset + 4, column=9)

        self.max_guests_venue_label.grid(row=row_offset + 5, column=8)
        self.max_guests_venue_entry.grid(row=row_offset + 5, column=9)

        self.venue_price_label.grid(row=row_offset + 6, column=8)
        self.venue_price_entry.grid(row=row_offset + 6, column=9)

        self.venue_dress_code_label.grid(row=row_offset + 7, column=8)
        self.venue_dress_code_entry.grid(row=row_offset + 7, column=9)

        self.venue_amenities_label.grid(row=row_offset + 8, column=8)
        self.venue_amenities_entry.grid(row=row_offset + 8, column=9)

        self.caterer_id_label.grid(row=row_offset + 9, column=8)
        self.caterer_id_entry.grid(row=row_offset + 9, column=9)

        self.caterer_name_label.grid(row=row_offset + 10, column=8)
        self.caterer_name_entry.grid(row=row_offset + 10, column=9)

        self.caterer_address_label.grid(row=row_offset + 11, column=8)
        self.caterer_address_entry.grid(row=row_offset + 11, column=9)

        self.caterer_phone_label.grid(row=row_offset + 12, column=8)
        self.caterer_phone_entry.grid(row=row_offset + 12, column=9)

        self.caterer_email_label.grid(row=row_offset + 13, column=8)
        self.caterer_email_entry.grid(row=row_offset + 13, column=9)

        self.caterer_instagram_label.grid(row=row_offset + 14, column=8)
        self.caterer_instagram_entry.grid(row=row_offset + 14, column=9)

        self.caterer_facebook_label.grid(row=row_offset + 15, column=8)
        self.caterer_facebook_entry.grid(row=row_offset + 15, column=9)

        self.caterer_menu_label.grid(row=row_offset + 16, column=8)
        self.caterer_menu_entry.grid(row=row_offset + 16, column=9)

        self.caterer_min_guests_label.grid(row=row_offset + 17, column=8)
        self.caterer_min_guests_entry.grid(row=row_offset + 17, column=9)

        self.caterer_max_guests_label.grid(row=row_offset + 18, column=8)
        self.caterer_max_guests_entry.grid(row=row_offset + 18, column=9)

        self.caterer_price_label.grid(row=row_offset + 19, column=8)
        self.caterer_price_entry.grid(row=row_offset + 19, column=9)

        self.caterer_client_id_label.grid(row=row_offset + 20, column=8)
        self.caterer_client_id_entry.grid(row=row_offset + 20, column=9)

        self.caterer_event_id_label.grid(row=row_offset + 21, column=8)
        self.caterer_event_id_entry.grid(row=row_offset + 21, column=9)

        self.caterer_equipment_label.grid(row=row_offset + 22, column=8)
        self.caterer_equipment_entry.grid(row=row_offset + 22, column=9)

        self.caterer_service_level_label.grid(row=row_offset + 23, column=8)
        self.caterer_service_level_entry.grid(row=row_offset + 23, column=9)

        self.caterer_setup_requirements_label.grid(row=row_offset + 24, column=8)
        self.caterer_setup_requirements_entry.grid(row=row_offset + 24, column=9)

        # (from here till line 803) :Place Employee, client , Supplier, Event, Guest,  buttons on the grid
        self.add_client_button.grid(row=19, column=2)
        self.delete_client_button.grid(row=19, column=3)
        self.modify_client_button.grid(row=20, column=2)
        self.display_clients_button.grid(row=20, column=3)
        self.display_single_client_button.grid(row=21, column=2, columnspan=2)
        self.add_supplier_button.grid(row=row_offset + 17, column=4)
        self.delete_supplier_button.grid(row=row_offset + 17, column=5)
        self.modify_supplier_button.grid(row=row_offset + 18, column=4)
        self.display_suppliers_button.grid(row=row_offset + 18, column=5)
        self.display_single_supplier_button.grid(row=row_offset + 19, column=4, columnspan=2)
        self.add_event_button.grid(row=row_offset + 21, column=6)
        self.delete_event_button.grid(row=row_offset + 21, column=7)
        self.modify_event_button.grid(row=row_offset + 22, column=6)
        self.display_events_button.grid(row=row_offset + 22, column=7)
        self.display_single_event_button.grid(row=row_offset + 25, column=8, columnspan=2)
        self.add_venue_button.grid(row=row_offset + 23, column=6)
        self.delete_venue_button.grid(row=row_offset + 23, column=7)
        self.modify_venue_button.grid(row=row_offset + 24, column=6)
        self.display_venues_button.grid(row=row_offset + 24, column=7)
        self.display_single_venue_button.grid(row=row_offset + 26, column=8, columnspan=2)
        self.add_catering_button.grid(row=row_offset + 25, column=6)
        self.delete_catering_button.grid(row=row_offset + 25, column=7)
        self.modify_catering_button.grid(row=row_offset + 26, column=6)
        self.display_catering_button.grid(row=row_offset + 26, column=7)
        self.display_single_catering_button.grid(row=row_offset + 27, column=8, columnspan=2)

        # These lines Initializes  list for each of the classes to store the information
        self.employees = [] # List to store employee objects
        self.clients = [] # List to store clients objects
        self.events = [] # List to store events objects
        self.suppliers = [] # List to store suppliers objects
        self.caterers = [] # List to store caterers objects
        self.venues = [] # List to store venues objects

    def add_employee(self): #This line defines a method 'add_employee'
        employee_id = self.employee_id_entry.get() # This line  retrieves the employee ID entered in the entry widget
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        nationality = self.nationality_entry.get()
        years_of_experience = self.years_of_experience_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        employee = Employee(employee_id, first_name, last_name, department, job_title, basic_salary, age, gender,
                            date_of_birth, nationality, years_of_experience, phone_number, email)
        self.employees.append(employee)

        messagebox.showinfo("Success", "Employee added successfully")

        # Clear entry fields
        self.clear_entries()

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()

        for index, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                del self.employees[index]
                messagebox.showinfo("Success", "Employee deleted successfully")
                break
        else:
            messagebox.showerror("Error", "Employee not found")

        # Clear entry fields
        self.clear_entries()

    def modify_employee(self):
        employee_id = self.employee_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        nationality = self.nationality_entry.get()
        years_of_experience = self.years_of_experience_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.first_name = first_name
                employee.last_name = last_name
                employee.department = department
                employee.job_title = job_title
                employee.basic_salary = basic_salary
                employee.age = age
                employee.gender = gender
                employee.date_of_birth = date_of_birth
                employee.nationality = nationality
                employee.years_of_experience = years_of_experience
                employee.phone_number = phone_number
                employee.email = email
                messagebox.showinfo("Success", "Employee modified successfully")
                break
        else:
            messagebox.showerror("Error", "Employee not found")

        # Clear entry fields
        self.clear_entries()

    def display_employees(self):
        if not self.employees:
            messagebox.showinfo("Info", "No employees to display")
            return

        display_text = ""
        for employee in self.employees:
            display_text += f"Employee ID: {employee.employee_id}, First Name: {employee.first_name}, Last Name: {employee.last_name}, Department: {employee.department}, Job Title: {employee.job_title}, Basic Salary: {employee.basic_salary}, Age: {employee.age}, Gender: {employee.gender}, Date of Birth: {employee.date_of_birth}, Nationality: {employee.nationality}, Years of Experience: {employee.years_of_experience}, Phone Number: {employee.phone_number}, Email: {employee.email}\n"

        messagebox.showinfo("Employees", display_text)

    def display_single_employee(self):
        employee_id = self.employee_id_entry.get()

        for employee in self.employees:
            if employee.employee_id == employee_id:
                display_text = f"Employee ID: {employee.employee_id}, First Name: {employee.first_name}, Last Name: {employee.last_name}, Department: {employee.department}, Job Title: {employee.job_title}, Basic Salary: {employee.basic_salary}, Age: {employee.age}, Gender: {employee.gender}, Date of Birth: {employee.date_of_birth}, Nationality: {employee.nationality}, Years of Experience: {employee.years_of_experience}, Phone Number: {employee.phone_number}, Email: {employee.email}"
                messagebox.showinfo("Employee Details", display_text)
                break
        else:
            messagebox.showerror("Error", "Employee not found")

        # Clear entry fields
        self.clear_entries()

    def clear_entries(self):
        self.employee_id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.date_of_birth_entry.delete(0, tk.END)
        self.nationality_entry.delete(0, tk.END)
        self.years_of_experience_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def add_client(self):
        client_id = self.client_id_entry.get()
        first_name = self.client_first_name_entry.get()
        last_name = self.client_last_name_entry.get()
        gender = self.client_gender_entry.get()
        number = self.client_number_entry.get()
        email = self.client_email_entry.get()
        num_of_guests = self.client_num_of_guests_entry.get()
        budget = self.client_budget_entry.get()
        event_type = self.client_event_type_entry.get()
        address = self.client_address_entry.get()
        event_preference = self.client_event_preference_entry.get()
        event_history = self.client_event_history_entry.get()
        communication_method = self.client_communication_method_entry.get()
        event_date_flexibility = self.client_event_date_flexibility_entry.get()
        event_theme_preferences = self.client_event_theme_preferences_entry.get()
        special_requests = self.client_special_requests_entry.get()
        referral_source = self.client_referral_source_entry.get()
        follow_up_history = self.client_follow_up_history_entry.get()
        event_timeline = self.client_event_timeline_entry.get()

        client = Client(client_id, first_name, last_name, gender, number, email, num_of_guests, budget, event_type,
                        address, event_preference, event_history, communication_method, event_date_flexibility,
                        event_theme_preferences, special_requests, referral_source, follow_up_history, event_timeline)
        self.clients.append(client)

        messagebox.showinfo("Success", "Client added successfully")

        # Clear entry widgets
        self.clear_client_entries()

    def delete_client(self):
        client_id = self.client_id_entry.get()

        for index, client in enumerate(self.clients):
            if client.client_id == client_id:
                del self.clients[index]
                messagebox.showinfo("Success", "Client deleted successfully")
                break
        else:
            messagebox.showerror("Error", "Client not found")

        # Clear entry widget
        self.clear_client_entries()

    def modify_client(self):
        client_id = self.client_id_entry.get()
        # Find the client by ID
        for client in self.clients:
            if client.client_id == client_id:
                # Update client details
                client.first_name = self.client_first_name_entry.get()
                client.last_name = self.client_last_name_entry.get()
                client.gender = self.client_gender_entry.get()
                client.number = self.client_number_entry.get()
                client.email = self.client_email_entry.get()
                client.num_of_guests = self.client_num_of_guests_entry.get()
                client.budget = self.client_budget_entry.get()
                client.event_type = self.client_event_type_entry.get()
                client.address = self.client_address_entry.get()
                client.event_preference = self.client_event_preference_entry.get()
                client.event_history = self.client_event_history_entry.get()
                client.communication_method = self.client_communication_method_entry.get()
                client.event_date_flexibility = self.client_event_date_flexibility_entry.get()
                client.event_theme_preferences = self.client_event_theme_preferences_entry.get()
                client.special_requests = self.client_special_requests_entry.get()
                client.referral_source = self.client_referral_source_entry.get()
                client.follow_up_history = self.client_follow_up_history_entry.get()
                client.event_timeline = self.client_event_timeline_entry.get()

                messagebox.showinfo("Success", "Client modified successfully")
                break
        else:
            messagebox.showerror("Error", "Client not found")

        # Clear entry widgets
        self.clear_client_entries()

    def display_clients(self):
        if not self.clients:
            messagebox.showinfo("Info", "No clients to display")
            return

        display_text = ""
        for client in self.clients:
            display_text += f"Client ID: {client.client_id}, First Name: {client.first_name}, Last Name: {client.last_name}, Email: {client.email}\n"

        messagebox.showinfo("Clients", display_text)

    def display_single_client(self):
        client_id = self.client_id_entry.get()

        for client in self.clients:
            if client.client_id == client_id:
                display_text = f"Client ID: {client.client_id}, First Name: {client.first_name}, Last Name: {client.last_name}, Gender: {client.gender}, Number: {client.number}, Email: {client.email}, Budget: {client.budget}, Event Type: {client.event_type}\n"
                # Add other fields as needed
                messagebox.showinfo("Client Details", display_text)
                break
        else:
            messagebox.showerror("Error", "Client not found")

        # Clear entry widget
        self.clear_client_entries()

    def clear_client_entries(self):
        self.client_id_entry.delete(0, tk.END)
        self.client_first_name_entry.delete(0, tk.END)
        self.client_last_name_entry.delete(0, tk.END)
        self.client_gender_entry.delete(0, tk.END)
        self.client_number_entry.delete(0, tk.END)
        self.client_email_entry.delete(0, tk.END)
        self.client_num_of_guests_entry.delete(0, tk.END)
        self.client_budget_entry.delete(0, tk.END)
        self.client_event_type_entry.delete(0, tk.END)
        self.client_address_entry.delete(0, tk.END)
        self.client_event_preference_entry.delete(0, tk.END)
        self.client_event_history_entry.delete(0, tk.END)
        self.client_communication_method_entry.delete(0, tk.END)
        self.client_event_date_flexibility_entry.delete(0, tk.END)
        self.client_event_theme_preferences_entry.delete(0, tk.END)
        self.client_special_requests_entry.delete(0, tk.END)
        self.client_referral_source_entry.delete(0, tk.END)
        self.client_follow_up_history_entry.delete(0, tk.END)
        self.client_event_timeline_entry.delete(0, tk.END)

    def add_supplier(self):
        # Get supplier details from entry widgets
        supplier_details = {
            "ID": self.supplier_id_entry.get(),
            "name": self.supplier_name_entry.get(),
            "Email": self.supplier_email_entry.get(),
            "Phone number": self.supplier_phone_number_entry.get(),
            "Pricing": self.supplier_pricing_entry.get(),
            "credit terms": self.supplier_credit_terms_entry.get(),
            "payment terms": self.supplier_payment_terms_entry.get(),
            "Shipping": self.supplier_shipping_entry.get(),
            "Supplier specialization": self.supplier_specialization_entry.get(),
            "Service area": self.supplier_service_area_entry.get(),
            "Availability": self.supplier_availability_entry.get(),
            "Quality assurance": self.supplier_quality_assurance_entry.get(),
            "Supplier ratings/reviews": self.supplier_ratings_reviews_entry.get(),
            "Preferred communication method": self.supplier_preferred_communication_entry.get(),
            "Contract details": self.supplier_contract_details_entry.get(),
            "Feedback history": self.supplier_feedback_history_entry.get(),
            "Payment history": self.supplier_payment_history_entry.get()
        }

        # Add supplier to the list
        self.suppliers.append(supplier_details)

        messagebox.showinfo("Success", "Supplier added successfully")

        # Clear entry widgets
        self.clear_supplier_entries()

    def delete_supplier(self):
        # Get supplier ID from entry widget
        supplier_id = self.supplier_id_entry.get()

        # Search and delete the supplier
        for supplier in self.suppliers:
            if supplier["ID"] == supplier_id:
                self.suppliers.remove(supplier)
                # Show success message
                messagebox.showinfo("Success", "Supplier deleted successfully.")
                break
        else:
            # Show error message if supplier not found
            messagebox.showerror("Error", "Supplier not found.")

        # Clear entry widget
        self.clear_supplier_entries()

    def modify_supplier(self):
        # Get supplier ID from entry widget
        supplier_id = self.supplier_id_entry.get()

        # Search and modify the supplier
        for supplier in self.suppliers:
            if supplier["ID"] == supplier_id:
                # Update supplier details
                supplier["name"] = self.supplier_name_entry.get()
                supplier["Email"] = self.supplier_email_entry.get()
                supplier["Phone number"] = self.supplier_phone_number_entry.get()
                supplier["Pricing"] = self.supplier_pricing_entry.get()
                supplier["credit terms"] = self.supplier_credit_terms_entry.get()
                supplier["payment terms"] = self.supplier_payment_terms_entry.get()
                supplier["Shipping"] = self.supplier_shipping_entry.get()
                supplier["Supplier specialization"] = self.supplier_specialization_entry.get()
                supplier["Service area"] = self.supplier_service_area_entry.get()
                supplier["Availability"] = self.supplier_availability_entry.get()
                supplier["Quality assurance"] = self.supplier_quality_assurance_entry.get()
                supplier["Supplier ratings/reviews"] = self.supplier_ratings_reviews_entry.get()
                supplier["Preferred communication method"] = self.supplier_preferred_communication_entry.get()
                supplier["Contract details"] = self.supplier_contract_details_entry.get()
                supplier["Feedback history"] = self.supplier_feedback_history_entry.get()
                supplier["Payment history"] = self.supplier_payment_history_entry.get()

                # Show success message
                messagebox.showinfo("Success", "Supplier modified successfully.")
                break
        else:
            # Show error message if supplier not found
            messagebox.showerror("Error", "Supplier not found.")

        # Clear entry widget
        self.clear_supplier_entries()

    def display_single_supplier(self):
        # Get supplier ID from entry widget
        supplier_id = self.supplier_id_entry.get()

        # Search and display the supplier details in a messagebox
        for supplier in self.suppliers:
            if supplier["ID"] == supplier_id:
                message = ""
                for key, value in supplier.items():
                    message += f"{key}: {value}\n"

                # Show supplier details
                messagebox.showinfo("Supplier Details", message)
                break
        else:
            # Show error message if supplier not found
            messagebox.showerror("Error", "Supplier not found.")

        # Clear entry widget
        self.clear_supplier_entries()

    def display_suppliers(self):
        if not self.suppliers:
            messagebox.showinfo("Info", "No suppliers to display")
            return

        display_text = ""
        for supplier in self.suppliers:
            for key, value in supplier.items():
                display_text += f"{key}: {value}\n"
            display_text += "\n"  # Add a new line between each supplier

        messagebox.showinfo("Suppliers", display_text)
    def clear_supplier_entries(self):
        # Clear all entry widgets for supplier
        self.supplier_id_entry.delete(0, tk.END)
        self.supplier_name_entry.delete(0, tk.END)
        self.supplier_email_entry.delete(0, tk.END)
        self.supplier_phone_number_entry.delete(0, tk.END)
        self.supplier_pricing_entry.delete(0, tk.END)
        self.supplier_credit_terms_entry.delete(0, tk.END)
        self.supplier_payment_terms_entry.delete(0, tk.END)
        self.supplier_shipping_entry.delete(0, tk.END)
        self.supplier_specialization_entry.delete(0, tk.END)
        self.supplier_service_area_entry.delete(0, tk.END)
        self.supplier_availability_entry.delete(0, tk.END)
        self.supplier_quality_assurance_entry.delete(0, tk.END)
        self.supplier_ratings_reviews_entry.delete(0, tk.END)
        self.supplier_preferred_communication_entry.delete(0, tk.END)
        self.supplier_contract_details_entry.delete(0, tk.END)
        self.supplier_feedback_history_entry.delete(0, tk.END)
        self.supplier_payment_history_entry.delete(0, tk.END)

    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contact = self.venue_contact_entry.get()
        min_guests = self.min_guests_venue_entry.get()
        max_guests = self.max_guests_venue_entry.get()
        price = self.venue_price_entry.get()
        dress_code = self.venue_dress_code_entry.get()
        amenities = self.venue_amenities_entry.get()
        availability = self.venue_availability_entry.get()
        capacity = self.venue_capacity_entry.get()
        photos = self.venue_photos_entry.get()
        layout = self.venue_layout_entry.get()

        venue = Venue(venue_id, name, address, contact, min_guests, max_guests, price, dress_code, amenities,
                      availability, capacity, photos, layout)
        self.venues.append(venue)

        messagebox.showinfo("Success", "Venue added successfully")

        # Clear entry fields
        self.clear_entries()

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()

        # Search and delete the venue
        for venue in self.venues:
            if venue.venue_ID == venue_id:
                self.venues.remove(venue)
                # Show success message
                messagebox.showinfo("Success", "Venue deleted successfully.")
                break
        else:
            # Show error message if venue not found
            messagebox.showerror("Error", "Venue not found.")

        # Clear entry widget
        self.clear_entries()

    def modify_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contact = self.venue_contact_entry.get()
        min_guests = self.min_guests_venue_entry.get()
        max_guests = self.max_guests_venue_entry.get()
        price = self.venue_price_entry.get()
        dress_code = self.venue_dress_code_entry.get()
        amenities = self.venue_amenities_entry.get()
        availability = self.venue_availability_entry.get()
        capacity = self.venue_capacity_entry.get()
        photos = self.venue_photos_entry.get()
        layout = self.venue_layout_entry.get()

        for venue in self.venues:
            if venue.venue_ID == venue_id:
                venue.name = name
                venue.address = address
                venue.contact = contact
                venue.min_guests = min_guests
                venue.max_guests = max_guests
                venue.price = price
                venue.dress_code = dress_code
                venue.amenities = amenities
                venue.availability = availability
                venue.capacity = capacity
                venue.photos = photos
                venue.layout = layout
                messagebox.showinfo("Success", "Venue modified successfully")
                break
        else:
            messagebox.showerror("Error", "Venue not found")

        # Clear entry fields
        self.clear_entries()

    def display_venues(self):
        if not self.venues:
            messagebox.showinfo("Info", "No venues to display")
            return

        display_text = ""
        for venue in self.venues:
            for key, value in vars(venue).items():
                display_text += f"{key}: {value}\n"
            display_text += "\n"  # Add a new line between each venue

        messagebox.showinfo("Venues", display_text)

    def display_single_venue(self):
        venue_id = self.venue_id_entry.get()

        # Search and display the venue details in a messagebox
        for venue in self.venues:
            if venue.venue_ID == venue_id:
                message = ""
                for key, value in vars(venue).items():
                    message += f"{key}: {value}\n"

                # Show venue details
                messagebox.showinfo("Venue Details", message)
                break
        else:
            # Show error message if venue not found
            messagebox.showerror("Error", "Venue not found.")

        # Clear entry widget
        self.clear_entries()


    def clear_entries(self):
        self.venue_id_entry.delete(0, tk.END)
        self.venue_name_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.venue_contact_entry.delete(0, tk.END)
        self.min_guests_venue_entry.delete(0, tk.END)
        self.max_guests_venue_entry.delete(0, tk.END)
        self.venue_price_entry.delete(0, tk.END)
        self.venue_dress_code_entry.delete(0, tk.END)
        self.venue_amenities_entry.delete(0, tk.END)
        self.venue_availability_entry.delete(0, tk.END)
        self.venue_capacity_entry.delete(0, tk.END)
        self.venue_photos_entry.delete(0, tk.END)
        self.venue_layout_entry.delete(0, tk.END)

    def add_caterer(self):
        caterer_id = self.caterer_id_entry.get()
        name = self.caterer_name_entry.get()
        address = self.caterer_address_entry.get()
        phone_number = self.caterer_phone_entry.get()
        email = self.caterer_email_entry.get()
        instagram = self.caterer_instagram_entry.get()
        facebook = self.caterer_facebook_entry.get()
        menu = self.caterer_menu_entry.get()
        min_guests = self.caterer_min_guests_entry.get()
        max_guests = self.caterer_max_guests_entry.get()
        price = self.caterer_price_entry.get()
        client_id = self.caterer_client_id_entry.get()
        event_id = self.caterer_event_id_entry.get()
        equipment = self.caterer_equipment_entry.get()
        service_level = self.caterer_service_level_entry.get()
        setup_requirements = self.caterer_setup_requirements_entry.get()

        caterer = CateringCompany(caterer_id, name, address, phone_number, email, instagram, facebook, menu, min_guests,
                          max_guests, price, client_id, event_id, equipment, service_level, setup_requirements)
        self.caterers.append(caterer)

        messagebox.showinfo("Success", "Caterer added successfully")

        # Clear entry fields
        self.clear_entries()

    def delete_caterer(self):
        caterer_id = self.caterer_id_entry.get()

        for index, caterer in enumerate(self.caterers):
            if caterer.caterer_ID == caterer_id:  # Make sure the attribute name matches
                del self.caterers[index]
                messagebox.showinfo("Success", "Caterer deleted successfully")
                break
        else:
            messagebox.showerror("Error", "Caterer not found")

        # Clear entry fields
        self.clear_entries()

    def modify_caterer(self):
        caterer_id = self.caterer_id_entry.get()
        name = self.caterer_name_entry.get()
        address = self.caterer_address_entry.get()
        phone_number = self.caterer_phone_entry.get()
        email = self.caterer_email_entry.get()
        instagram = self.caterer_instagram_entry.get()
        facebook = self.caterer_facebook_entry.get()
        menu = self.caterer_menu_entry.get()
        min_guests = self.caterer_min_guests_entry.get()
        max_guests = self.caterer_max_guests_entry.get()
        price = self.caterer_price_entry.get()
        client_id = self.caterer_client_id_entry.get()
        event_id = self.caterer_event_id_entry.get()
        equipment = self.caterer_equipment_entry.get()
        service_level = self.caterer_service_level_entry.get()
        setup_requirements = self.caterer_setup_requirements_entry.get()

        for caterer in self.caterers:
            if caterer.caterer_ID == caterer_id:
                caterer.name = name
                caterer.address = address
                caterer.phone_number = phone_number
                caterer.email = email
                caterer.instagram = instagram
                caterer.facebook = facebook
                caterer.menu = menu
                caterer.min_guests = min_guests
                caterer.max_guests = max_guests
                caterer.price = price
                caterer.client_id = client_id
                caterer.event_id = event_id
                caterer.equipment = equipment
                caterer.service_level = service_level
                caterer.setup_requirements = setup_requirements
                messagebox.showinfo("Success", "Caterer modified successfully")
                break
        else:
            messagebox.showerror("Error", "Caterer not found")

        # Clear entry fields
        self.clear_entries()

    def display_caterers(self):
        if not self.caterers:
            messagebox.showinfo("Info", "No caterers to display")
            return

        display_text = ""
        for caterer in self.caterers:
            for key, value in caterer.__dict__.items():
                display_text += f"{key}: {value}\n"
            display_text += "\n"  # Add a new line between each caterer

        messagebox.showinfo("Caterers", display_text)

    def display_single_catering(self):
        # Get caterer ID from entry widget
        caterer_id = self.caterer_id_entry.get()

        # Search and display the caterer details in a messagebox
        for caterer in self.caterers:
            if caterer.caterer_ID == caterer_id:
                message = ""
                for key, value in caterer.__dict__.items():
                    message += f"{key}: {value}\n"

                # Show caterer details
                messagebox.showinfo("Caterer Details", message)
                break
        else:
            # Show error message if caterer not found
            messagebox.showerror("Error", "Caterer not found.")

        # Clear entry widget
        self.clear_entries()
    def clear_entries(self):
        self.caterer_id_entry.delete(0, tk.END)
        self.caterer_name_entry.delete(0, tk.END)
        self.caterer_address_entry.delete(0, tk.END)
        self.caterer_phone_entry.delete(0, tk.END)
        self.caterer_email_entry.delete(0, tk.END)
        self.caterer_instagram_entry.delete(0, tk.END)
        self.caterer_facebook_entry.delete(0, tk.END)
        self.caterer_menu_entry.delete(0, tk.END)
        self.caterer_min_guests_entry.delete(0, tk.END)
        self.caterer_max_guests_entry.delete(0, tk.END)
        self.caterer_price_entry.delete(0, tk.END)
        self.caterer_client_id_entry.delete(0, tk.END)
        self.caterer_event_id_entry.delete(0, tk.END)
        self.caterer_equipment_entry.delete(0, tk.END)
        self.caterer_service_level_entry.delete(0, tk.END)
        self.caterer_setup_requirements_entry.delete(0, tk.END)

    def add_event(self):
        event_id = self.event_id_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        title = self.title_entry.get()
        type_of_event = self.type_of_event_entry.get()
        address = self.address_entry.get()
        duration = self.duration_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        venue = self.venue_entry.get()
        theme = self.theme_entry.get()
        num_of_guests = self.num_of_guests_entry.get()
        min_of_guests = self.min_of_guests_entry.get()
        music = self.music_entry.get()
        giveaways = self.giveaways_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()
        event_budget = self.event_budget_entry.get()
        event_marketing_materials = self.event_marketing_materials_entry.get()
        event_sponsorships = self.event_sponsorships_entry.get()

        event = Event(event_id, date, time, title, type_of_event, address, duration, guest_list, catering_company,
                      cleaning_company, decorations_company, venue, theme, num_of_guests, min_of_guests,
                      music,
                      giveaways, entertainment_company, furniture_supply_company, invoice, event_budget,
                      event_marketing_materials, event_sponsorships)
        self.events.append(event)

        messagebox.showinfo("Success", "Event added successfully")

        # Clear entry fields
        self.clear_entries()


    def delete_event(self):
        event_id = self.event_id_entry.get()

        for index, event in enumerate(self.events):
            if event.event_ID == event_id:
                del self.events[index]
                messagebox.showinfo("Success", "Event deleted successfully")
                break
        else:
            messagebox.showerror("Error", "Event not found")

        # Clear entry fields
        self.clear_entries()

    def modify_event(self):
        event_id = self.event_id_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        title = self.title_entry.get()
        type_of_event = self.type_of_event_entry.get()
        address = self.address_entry.get()
        duration = self.duration_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        cleaning_company = self.cleaning_company_entry.get()
        decorations_company = self.decorations_company_entry.get()
        venue = self.venue_entry.get()
        theme = self.theme_entry.get()
        num_of_guests = self.num_of_guests_entry.get()
        min_of_guests = self.min_of_guests_entry.get()
        music = self.music_entry.get()
        giveaways = self.giveaways_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_supply_company = self.furniture_supply_company_entry.get()
        invoice = self.invoice_entry.get()
        event_budget = self.event_budget_entry.get()
        event_marketing_materials = self.event_marketing_materials_entry.get()
        event_sponsorships = self.event_sponsorships_entry.get()

        for event in self.events:
            if event.event_ID == event_id:
                event.date = date
                event.time = time
                event.title = title
                event.type_of_event = type_of_event
                event.address = address
                event.duration = duration
                event.guest_list = guest_list
                event.catering_company = catering_company
                event.cleaning_company = cleaning_company
                event.decorations_company = decorations_company
                event.venue = venue
                event.theme = theme
                event.num_of_guests = num_of_guests
                event.min_of_guests = min_of_guests
                event.music = music
                event.giveaways = giveaways
                event.entertainment_company = entertainment_company
                event.furniture_supply_company = furniture_supply_company
                event.invoice = invoice
                event.event_budget = event_budget
                event.event_marketing_materials = event_marketing_materials
                event.event_sponsorships = event_sponsorships
                messagebox.showinfo("Success", "Event modified successfully")
                break
        else:
            messagebox.showerror("Error", "Event not found")

        # Clear entry fields
        self.clear_entries()

    def display_single_event(self):
        event_id = self.event_id_entry.get()
        for event in self.events:
            if event.event_ID == event_id:
                message = ""
                for key, value in event.__dict__.items():
                    message += f"{key}: {value}\n"

                messagebox.showinfo("Event Details", message)
                break
        else:
            messagebox.showerror("Error", "Event not found.")


    def display_events(self):
        if not self.events:
            messagebox.showinfo("Info", "No events to display")
            return

        display_text = ""
        for event in self.events:
            for key, value in vars(event).items():
                display_text += f"{key}: {value}\n"
            display_text += "\n"  # Add a new line between each event

        messagebox.showinfo("Events", display_text)
        self.clear_entries()

    def clear_entries(self):
        self.event_id_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.type_of_event_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.guest_list_entry.delete(0, tk.END)
        self.catering_company_entry.delete(0, tk.END)
        self.cleaning_company_entry.delete(0, tk.END)
        self.decorations_company_entry.delete(0, tk.END)
        self.venue_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.num_of_guests_entry.delete(0, tk.END)
        self.min_of_guests_entry.delete(0, tk.END)
        self.music_entry.delete(0, tk.END)
        self.giveaways_entry.delete(0, tk.END)
        self.entertainment_company_entry.delete(0, tk.END)
        self.furniture_supply_company_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)
        self.event_budget_entry.delete(0, tk.END)
        self.event_marketing_materials_entry.delete(0, tk.END)
        self.event_sponsorships_entry.delete(0, tk.END)
    def save_data(self):
        with open('employees.pkl', 'wb') as file:
            pickle.dump(self.employees, file)

        with open('clients.pkl', 'wb') as file:
            pickle.dump(self.clients, file)

        with open('events.pkl', 'wb') as file:
            pickle.dump(self.events, file)

        with open('suppliers.pkl', 'wb') as file:
            pickle.dump(self.suppliers, file)

        with open('caterers.pkl', 'wb') as file:
            pickle.dump(self.caterers, file)

        with open('venues.pkl', 'wb') as file:
            pickle.dump(self.venues, file)


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='light blue')
    app = EventManagementsystem(root)
    root.mainloop()
    app.save_data()

