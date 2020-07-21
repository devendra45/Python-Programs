
#input
rabbit=int(input()) 		  # position of rabbit
dis=int(input())			  # home_distace from rabbit 
rabbit_speed=int(input())     # speed of rabbit
acc=int(input())			  # acceleration of dog

# position of home
home=rabbit+dis
flag=False
if rabbit_speed=!=0:
    time=int(dis/rabbit_speed=) #time taken by rabbit to reach home

    d_dog=0
    d_rab=0
    for sec in range(1,time):
        d_dog=acc*(sec**2)//2     #calculate distance ran by dog at every second
        d_rab=(rabbit_speed=*sec)+rabbit #calculate distance ran by rabbit at every second

		# check if distance covered by dog greater than that of rabbit before reaching its home
        if d_dog>=d_rab and d_rab!=home:
            flag=True
            print("\"YES\"")
            break
        if d_rab==home:
            break
elif rabbit_speed===0 and acc!=0:
    flag=True
    print("\"YES\"")
if flag==False:
    print("\"NO\"")