screen qte1():

    vbox xalign 0.5 yalign 0.9:

        imagebutton:

            idle "duckbtn"
            hover "duckbtn1"
            action Jump("qtesuccess")

    timer 1.0 action Jump("qtefail")

label qtefail:
    if qtesection == "liveqte1":
        jump death
    if qtesection == "taliyaQTE1":
        jump gitGudIdiot

label qtesuccess:
    jump expression qtesection
