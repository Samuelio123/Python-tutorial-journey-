#  I want to print how my church sunday service program goes.
sun_service = ["1. Open Heaven devotion", "2. Workers meeting", "3. Sunday school", "4. Praise and Worship", "5. Opening prayer", "6. Bible reading", "7. Announcement", "8. Choir ministration", "9. Sermon", "10. Closing prayer"]

print("Sunday service goes in this order:")

for i in sun_service:
    print(f"{i}")

user = input("-> ")

if user == "1":
    print("""This is the First session carried out every Sunday morning.
One of the Elders comes on to lead the congregation to read the open heaven devotion.""")
if user == "2":
    print("The Zonal pastor comes on to update the workers on the recent happenings and changes to be made pertaining to the church.")
if user == "3":
    print("Everybody goes to their various classes and take their sunday school manual.")
if user == "4":
    print("The choirs comes to lead us in praise and worship.")
if user == "5":
    print("One of the pastors will come to lead the church in the opening prayer.")
if user == "6":
    print("A pastor will come to take the Bible reading relating to the sermon.")
if user == "7":
    print("An appointed fellow will tell the congregation about the recent changes in the church policies.")
if user == "8":
    print("The choirs will comes on and minister to the congregation through melodious songs.")
if user == "9":
    print("""This is the main session in a Sunday program.
Here, the whole congregation sits down and listen to the word of God""")
if user == "10":
    print("""Here, The sunday service comes to an end.
The church takes their closing prayer, and then sings the Redeemer anthem.""")

