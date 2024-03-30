**Summary**
| Field | Detail |
|-------|--------|
| Project Name | Easy Money |
| Description | Easy Money is a budgeting app tracking income and expenses to help promote financial literacy. |
| Developers | Timothy Rodriguez |
| Live Website | https://unit4-be.onrender.com |
| Repo | https://github.com/timorodr/unit4-BE |

## Problem Being Solved and Target Market

Working in a nursing home I noticed how important financial literacy is to residents who aim to live independently. I built this for not only those individuals but for anyone who is trying to incresae their financial literacy.

## User Stories


- Users should be able to see the site on desktop and mobile
- Users can create an account
- Users can sign in to their account
- Users can create a new item
- Users can see all their items on the dashboard
- Users can update items
- User can delete items

## Route Tables

List of all routes and their functionality in the app

| Endpoint | Method | Response | Other |
| -------- | ------ | -------- | ----- |
| /budget | GET | JSON of all items | |
| /budget | POST | Create new item return JSON of new item | |
| /budget/:id | GET | JSON of item with matching id number | |
| /budget/:id | PUT | update item with matching id, return its JSON |  |
| /budget/:id | DELETE | delete the item with the matching id | |

## ERD
![My ERD](https://i.imgur.com/SbfizW6.png)
