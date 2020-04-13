from p5 import *
import time
import random
def box_with_lines_data(x,y,width,height,max_rows,data):
    j=1
    rect_mode("CORNER")
    rect((x,y),width,height)
    space_btw_array=height/max_rows
    for i in range(0,max_rows):
         line((x,y+space_btw_array*j),(x+width,y+space_btw_array*j))
         fill(0)
         text(data[i],(x+2,y+(space_btw_array*j)-8))
         no_fill()
         j+=1
def rand_hex(x,y):
    return str(hex(random.randrange(x,y,2)))
    
def setup():
    size(769,453)
    virtual_addr,PDPT,PD,index_PT,offset=rand_hex(0,2**32),rand_hex(0,3),rand_hex(0,2**9),rand_hex(0,2**9),rand_hex(0,2**12)
    print(virtual_addr,'    ',PDPT,'    ',PD,'    ',index_PT,'    ',offset)
    print(type(PD))
    data=[str(bin(random.randrange(0,3,1))) for i in range(0,4)]
    data_sec=[str(bin(random.randrange(0,20,3))) for i in range(0,20)]
    
        
def draw():
    background(256)
   
    #create random  value
    virtual_addr,PDPT,PD,index_PT,offset=rand_hex(0,2**32),rand_hex(0,3),rand_hex(0,2**9),rand_hex(0,2**9),rand_hex(0,2**12)
    data=[str(bin(random.randrange(0,3,1))) for i in range(0,4)]
    data_sec=[str(bin(random.randrange(0,20,3))) for i in range(0,20)]
    
    #shapes
    rect_mode("CORNER")
    rect((22,164),110,40)
    rect((233,102),155,311)
    box_with_lines_data(477,24,95,147,4,data)
    box_with_lines_data(612,119,125,311,20,data_sec)
    rect((256,264),107,43)
    rect((256,341),107,43)
    circle((308,163),50)
    line((308,263),(308,308))
    line((477,104),(384,152))
    circle((477,104),5)
    circle((384,152),5)
    line((382,310),(612,393))
    circle((382,310),5)
    circle((612,393),5)
    begin_shape()
    vertex(78,164)
    vertex(199,54)
    vertex(342,24)
    vertex(477,36)
    end_shape()
    circle((78,164),5)
    circle((477,36),5)
    

    # texts
    #text_size(32)
    fill(0)
    text("VIRTUAL ADDRESS",(23,239))
    text("PHYSICAL MEMORY (PM)",(640,89))
    text("TRANSMISSION LOOK AHEAD BUFFER (TLB)",(397,186))
    text("MMU",(247,75))
    text("The page is first looked up in the TLB ",(145,14))
    text("If no hit in the TLB ",(350,80))
    text("MMU maps to PM and add to table",(390,300))
    text(virtual_addr,(37,184))
    text(PDPT,(298,164))
    text(PD,(266,288))
    text(index_PT,(316,286))
    text(offset,(281,364))
    no_fill()

    #delay
    time.sleep(3)

    

    
   
if __name__ == '__main__':
    run()


"""
Rough Calculations
145,14  tlb line
399,90 tlb --mmu
466, 289  mmu---physical
 
"""
