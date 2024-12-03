import psutil
import tkinter as tk
import win32gui

# 获取 CPU 和内存利用率
def get_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    print(cpu_percent)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    return cpu_percent, memory_percent

# 更新窗口中的信息
def update_usage():
    cpu, memory = get_usage()
    label.config(text=f"CPU {cpu}% | 内存 {memory}%")
    window.after(1000, update_usage)  # 每秒更新一次

if __name__ == '__main__':
    # 创建 GUI 窗口
    window = tk.Tk()
    window.overrideredirect(True)
    # 创建标签显示 CPU 和内存利用率
    label = tk.Label(window, text="CPU 0% | Memory 0%", bg="#333333", fg="black")

    label.pack(fill="both", expand=True)

    m_hTaskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    # m_hBar = win32gui.FindWindowEx(m_hTaskbar, 0, "ReBarWindow32", None)
    # m_hMin = win32gui.FindWindowEx(m_hBar, 0, "MSTaskSwWClass", None)

    b = win32gui.GetWindowRect(m_hTaskbar)  # 获取m_hBar窗口尺寸b为[左，上，右，下]的数组
    window.geometry(f"150x24+{b[0]}+{b[1]-24}")

    window.attributes('-topmost', 1)  # 保持窗口始终在最前面
    window.config(bg='#333333')
    window.attributes('-transparentcolor', '#333333')  # 可选：设置透明背景
    window.resizable(False, False)  # 禁止调整窗口大小

    # 启动更新函数
    update_usage()
    # 运行窗口
    window.mainloop()