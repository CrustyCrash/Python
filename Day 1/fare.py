# Take the source, destination, fare in INR, discount_rate percentage from the user and display the
# string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"

print("Enter source")
source = input()
print("Enter destination")
destination = input()
print("Enter fare")
fare = int(input())
print("Enter discount")
discount = int(input())

print("Fare from", source, "to", destination, "is", fare, "INR,", "after applied discount of", discount, "% it is ",
      ((100-discount)/100)*fare, "INR")
