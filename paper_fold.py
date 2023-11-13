import time
start = time.time()

THICKNESS = 0.00008
times = 44

paper_thick = []
for i in range(times):
    folded_thickness = THICKNESS * 2
    THICKNESS = folded_thickness


elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))
print("Thickness: {: .2f} kilometers".format(folded_thickness / 1000))

print(f'Is time equal to {times} and {len(paper_thick)}?')

plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness [m]")
plt.plot(paper_thick, color=red)
plt.thick_params(labelsize = 20)
plt.show()
