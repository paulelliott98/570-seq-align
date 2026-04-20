import matplotlib.pyplot as plt
# input
sizes = [16,64,128,256,384,512,768,1024,1280,1536,2048,2560,3072,3584,3968]

time_basic = [0.1969,1.739,6.3519,24.421,61.1951,101.398,312.6581,630.0502,
              1034.6551,1544.76,2937.0062,4676.8179,6822.1831,9531.6219,11752.9869]

time_efficient = [0.2089,1.8458,6.3066,36.454,89.9901,170.5689,449.856,929.8849,
            1501.8373,2120.5609,4101.2132,6731.7181,9613.2948,13728.673,10201.192]

mem_basic = [13.4355,38.6182,152.4111,592.9385,1322.5557,2337.2549,5235.4424,
             9283.4072,14489.3643,20843.4775,37006.8564,57779.0674,83159.4854,
             113141.0244,138659.9775]

mem_efficient = [13.4355,39.165,152.958,301.9033,149.1895,230.6396,104.5342,
           200.1055,194.2949,233.8848,190.5039,191.7227,171.5791,200.8994,220.719]

# mark where both time_basic and mem_basic are smaller than time_efficient and mem_efficient
sweet_spot = []
for i in range(len(sizes)):
    if time_basic[i] < time_efficient[i] and mem_basic[i] < mem_efficient[i]:
        sweet_spot.append(i)

print("basic both smaller at:", [sizes[i] for i in sweet_spot])

# plot the line graph of time
plt.figure(figsize=(10, 5))
plt.plot(sizes, time_basic, marker='o', label='Basic')
plt.plot(sizes, time_efficient, marker='o', label='Efficient')
# highlight the sweet spot in red
for i in sweet_spot:
    plt.scatter(sizes[i], time_basic[i], color='red', s=80, zorder=5)
    plt.annotate(f"{sizes[i]}", (sizes[i], time_basic[i]),
                 textcoords="offset points", xytext=(0,10), ha='center', color='red')

plt.xlabel("M + N")
plt.ylabel("Time (ms)")
plt.title("Memory-efficient/Basic Version: Time vs. Problem Size Graph")
plt.legend()
plt.grid(True)
plt.show()

# plot the line graph of memory
plt.figure(figsize=(10, 5))
plt.plot(sizes, mem_basic, marker='o', label='Basic')
plt.plot(sizes, mem_efficient, marker='o', label='Efficient')
# highlight the sweet spot in red
for i in sweet_spot:
    plt.scatter(sizes[i], mem_basic[i], color='red', s=80, zorder=5)
    plt.annotate(f"{sizes[i]}", (sizes[i], mem_basic[i]),
                 textcoords="offset points", xytext=(0,10), ha='center', color='red')

plt.xlabel("M + N")
plt.ylabel("Memory (KB)")
plt.title("Memory-efficient/Basic Version: Memory vs. Problem Size Graph")
plt.legend()
plt.grid(True)
plt.show()

# plot a zoomed-in time graph for smaller input sizes (3)
time_size_small = sizes[:3]
time_basic_small = time_basic[:3]
time_eff_small = time_efficient[:3]

plt.figure()

plt.plot(time_size_small, time_basic_small, marker='o', label='Basic')
plt.plot(time_size_small, time_eff_small, marker='o', label='Efficient')

plt.xlabel("M + N")
plt.ylabel("Time (ms)")
plt.title("A Zoomed-in View of the Time vs. Problem Size Graph")
plt.legend()
plt.grid(True)
for i in range(len(time_size_small)):
    plt.annotate(f"{time_basic_small[i]:.1f}",
                 (time_size_small[i], time_basic_small[i]),
                 textcoords="offset points",
                 xytext=(0,10), ha='center',
                 color='tab:blue')
for i in range(len(time_size_small)):
    plt.annotate(f"{time_eff_small[i]:.1f}",
                 (time_size_small[i], time_eff_small[i]),
                 textcoords="offset points",
                 xytext=(0,-15), ha='center', 
                 color='tab:orange')
plt.show()

# plot a zoomed-in memory graph for smaller input sizes (4)
mem_size_small = sizes[:4]
mem_basic_small = mem_basic[:4]
mem_eff_small = mem_efficient[:4]

plt.figure()

plt.plot(mem_size_small, mem_basic_small, marker='o', label='Basic')
plt.plot(mem_size_small, mem_eff_small, marker='o', label='Efficient')

plt.xlabel("M + N")
plt.ylabel("Memory (ms)")
plt.title("A Zoomed-in View of the Memory vs. Problem Size Graph")
plt.legend()
plt.grid(True)
for i in range(len(mem_size_small)):
    plt.annotate(f"{mem_basic_small[i]:.1f}",
                 (mem_size_small[i], mem_basic_small[i]),
                 textcoords="offset points",
                 xytext=(0,10), ha='center',
                 color='tab:blue')
for i in range(len(mem_size_small)):
    plt.annotate(f"{mem_eff_small[i]:.1f}",
                 (mem_size_small[i], mem_eff_small[i]),
                 textcoords="offset points",
                 xytext=(0,-15), ha='center', 
                 color='tab:orange')
plt.show()