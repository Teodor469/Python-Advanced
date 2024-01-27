def hanoi(n, source_rod, target_rod, auxiliary_rod):
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {target_rod}")
        return
    hanoi(n - 1, source_rod, auxiliary_rod, target_rod)
    print(f"Move disk {n} from {source_rod} to {target_rod}")
    hanoi(n - 1, auxiliary_rod, target_rod, source_rod)

# Test the function
num_disks = 5
hanoi(num_disks, 'A', 'C', 'B')