# dressme
## Authors
- Aneesh Khera
- Cibi Pari
- Alan Shum
- Jayanth Sundaresan

## Purpose
A Django based web application using the to help users pick out tomorrow's outfits today. 


## Features
* Sync with calendar and give suggestion based on schedule
* Give suggestions based on weather
* Reminders of when to do laundry based on available clothing and necessary clothing
* Suggestions of unused clothing to throw out


## Control Flow
* Login page
* 
* Startup screen - logo
* Input screen - if no user data, prompt to set up new user household, else: show entire household as tableview with user's chore on top
* Setting up household: input all users and possible chores/due dates and frequency
* Ability to edit chores, reassign, remove
* Ability to check off chores

## Implementation
### Model
* User.swift
* Event.swift
* Outfit.swift

### View
* Login page
* Register
* Calendar
* Outfit options for today
* Other

### Controller
* LoginViewController
* RegisterViewController
* CalendarViewController
* OutfitViewController
* OtherViewController
