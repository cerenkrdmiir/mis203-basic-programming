from datetime import datetime
import time

machines = {1: "Available", 2: "Available", 3: "Available"}

print("=== DORM LAUNDRY SYSTEM ===")
print(f"System Start Time: {datetime.now().strftime('%H:%M:%S')}")

print("\nCurrent Machine Status:")
for no, status in machines.items():
  print(f"Machine {no}: {status}")

selected_machine = 1
student_name = "Ceren"

if machines[selected_machine] == "Available":
  machines[selected_machine] = f"Occupied by {student_name}"
  print(
      f"\n✓ Success: Machine {selected_machine} reserved for {student_name}."
  )


print("\nUpdating system, please wait...")
time.sleep(2)  # Pauses for 2 seconds

print("\n--- Updated Status ---")
for no, status in machines.items():
  print(f"Machine {no}: {status}")
