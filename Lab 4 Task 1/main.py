import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8')

l = np.linspace(0.1, 2*np.pi, 100)

z1 = 1 - (1/4) * (1/np.sin(3*l)**2) + 3*np.cos(2*l)
z2 = np.cos(3*l)**2 + np.sin(l)**4

fig1, ax1 = plt.subplots(figsize=(10, 6))

color1 = 'tab:blue'
ax1.set_xlabel('l')
ax1.set_ylabel('z1', color=color1)
line1 = ax1.plot(l, z1, color=color1, linewidth=2, label='z1 = 1 - (1/4)/sin²(3l) + 3cos(2l)')
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('z2', color=color2)
line2 = ax2.plot(l, z2, color=color2, linestyle='--', linewidth=2, label='z2 = cos²(3l) + sin⁴(l)')
ax2.tick_params(axis='y', labelcolor=color2)

ax1.set_title('Графики функций z1 и z2 с разными осями Y')
ax1.grid(True, alpha=0.3)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

# min_idx = np.argmin(z1)
# ax1.annotate('Локальный минимум z1', xy=(l[min_idx], z1[min_idx]), xytext=(l[min_idx]+0.5, z1[min_idx]+2),
#             arrowprops=dict(arrowstyle='->', color='blue'), fontsize=10)

plt.tight_layout()
plt.savefig('graph_two_functions.png', dpi=300, bbox_inches='tight')
plt.savefig('graph_two_functions.pdf', bbox_inches='tight')
plt.show()