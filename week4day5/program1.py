name = input("Student Name: ")
t = float(input("Tuition Fee: "))
l = float(input("Library Fee: "))
e = float(input("Exam Fee: "))

total = t + l + e
gst = total * 0.05
final = total + gst

print("\n--- Fee Receipt ---")
print("Name:", name)
print("Total Fee:", total)
print("GST:", gst)
print("Final Fee:", final)