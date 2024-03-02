screen duckQTE():
    vbox xalign 0.5 yalign 0.9:
        imagebutton:

            idle "duckbtn"
            hover "duckbtn1"
            action Jump("qtesuccess")

    timer 1.0 action Jump("qtefail")

label qtefail:
    if duckQTE == "cynthiaDQTE":
        jump lostCynthiaDQTE
    if duckQTE == "taliyaDQTE":
        jump gitGudIdiot

label qtesuccess:
    jump expression duckQTE
