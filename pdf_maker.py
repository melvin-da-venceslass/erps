from fpdf import FPDF
import os    

import datetime, time
                                                                           
class PDF(FPDF):
    pass

data = [{"id":"#",
         "desc":"Desc",
         "qty":"Qty",
         "cost":"Cost - INR",
         "gst":"GST %",
         "hsn":"HSN",
         "t_cost":"Total (INR)",
         "g_cost":"Total + GST (INR)"
        }]

def h_writer(w,x,y,z,pdf):
    pdf.set_xy(x,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=w, h=5.0, align='C', txt=str(z),border=1) 


def b_writer(w,x,y,z,pdf):
    pdf.set_xy(x,y)
    pdf.set_font('Montserrat Regular',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=w, h=5.0, align='C', txt=str(z),border=1) 
        

def invocie(_to,to_address,_to_comp,_date, _quote_id,_quoted_by,_validity,_leadTime,tdata,inclusive,exclusive,remarks):
    
    pdf = PDF(orientation='P', format='A4')
    pdf.add_page()
    #os.remove('test.pdf')
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.image("support/logo.jpg", x = 6.0, y = 10.0, w = 80.0, h = 40.0, type = '', link = '')


    pdf.set_xy(95,15)
    #pdf.set_font('f', '', 10, )
    pdf.add_font('Montserrat Regular', '', 'Montserrat-Regular.ttf', uni=True)
    pdf.add_font('Montserrat Bold', '', 'Montserrat-SemiBold.ttf', uni=True)
    pdf.set_font('Montserrat Bold', '', 10)
    pdf.set_text_color(71,71,71)
    pdf.cell(w=110.0, h=5.0, align='C', txt="MELVIN & VENFRA INNOVATIVE INDUSTRIAL SOLUTIONS",border=0)
    pdf.set_xy(95,22)
    pdf.set_font('Montserrat Regular',"", 10)
    pdf.multi_cell(w=110.0, h=5.0, align='C', txt="#142, Vencie's Garden South Street, Panikankuppam, Panruti, Cuddalore, Tamilnadu, India 607106",border=0)



    pdf.set_xy(95,34)
    pdf.set_font('Montserrat Regular',"", 9)
    pdf.set_text_color(0, 0, 255)
    pdf.cell(w=110.0, h=5.0, align='C', txt="Email: melvin.venfra@gmail.com  |  Ph: +91 805 675 9527  ",border=0) 
    pdf.line(10.0,55.0,200.0,55.0)

    titles =["Quotation#","Date#", "Validity#","Lead-Time","Payment type","Quoted By"] 
    for each in range(6):
        m = 31.5
        y = (each*m)+10.5
        pdf.set_xy(y,58.0)
        pdf.set_font('Montserrat Bold',"", 9)
        pdf.set_text_color(71,71,71)
        pdf.cell(w=m, h=6.0, align='L', txt=titles[each],border=1) 


    def quoted_by():
        return "Melvin Paul Miki"

    titles= [_quote_id , _date, _validity,_leadTime,"NTFS | IMPS",_quoted_by]
    for each in range(6):
        m = 31.5
        y = (each*m)+10.5
        pdf.set_xy(y,64.0)
        pdf.set_font('Montserrat Regular',"", 9)
        pdf.set_text_color(71,71,71)
        pdf.multi_cell(w=m, h=6.0, align='C', txt=titles[each],border=1) 

        
    #pdf.line(10.0,73.0,200.0,73.0)

    titles =["GSTN#","Bank", "Branch","Account#","IFSC"] 
    for each in range(5):
        m = 37.8
        y = (each*m)+10.5
        pdf.set_xy(y,76.0)
        pdf.set_font('Montserrat Bold',"", 9)
        pdf.set_text_color(71,71,71)
        pdf.cell(w=m, h=6.0, align='L', txt=titles[each],border=1) 

    
        
    titles =["33FHGPM2821H1ZI","Axis Bank", "Panruti","921020008101730","UTIB000416"] 
    for each in range(5):
        m = 37.8
        y = (each*m)+10.5
        pdf.set_xy(y,82.0)
        pdf.set_font('Montserrat regular',"", 9)
        pdf.set_text_color(71,71,71)
        pdf.cell(w=m, h=6.0, align='L', txt=titles[each],border=1) 
        
    pdf.line(10.0,91.0,200.0,91.0)

    pdf.set_xy(10.0,93.0)
    pdf.set_font('Montserrat Bold',"", 12)
    pdf.set_text_color(71,71,71)
    pdf.cell(w=70.0, h=5.0, align='L', txt="To:",border=0) 

    pdf.set_xy(20.0,93.0)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.cell(w=70.0, h=5.0, align='L', txt=_to,border=0) 

    pdf.set_xy(20.0,98.0)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.cell(w=70.0, h=5.0, align='L', txt=_to_comp,border=0) 

    pdf.set_xy(20,105.0)
    pdf.set_font('Montserrat Regular',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=70.0, h=5.0, align='L', txt=to_address,border=0) 


    pdf.line(100.0,93.0,100.0,119.0)

    pdf.set_xy(105,93.0)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=70.0, h=5.0, align='L', txt="Payment Terms",border=0) 

    pdf.set_xy(105,98.0)
    pdf.set_font('Montserrat regular',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=70.0, h=5.0, align='L', txt="60% advance along with PO.",border=0) 


    pdf.set_xy(105,103.0)
    pdf.set_font('Montserrat regular',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=70.0, h=5.0, align='L', txt="30% During Dispatch.",border=0)

    pdf.set_xy(105,108.0)
    pdf.set_font('Montserrat regular',"", 9)
    pdf.set_text_color(71,71,71)
    pdf.multi_cell(w=70.0, h=3.0, align='L', txt="Remaining 10% in 30 days after delivery or installation, which ever is earlier.",border=0) 

    pdf.line(10.0,121.0,200.0,121.0)


    titles =["S.No#","Desc","","HSN","Cost - INR","Qty","Cost - INR","GST%","Total - INR"] 

  


    for idx,each in enumerate(data):
        leng,x,y=[20.1,10.0,126.0]
        h_writer(leng/2,x,y,each["id"],pdf)
        
        x =x+leng/2
        h_writer(leng+(leng/2),x,y,each["desc"],pdf)
        
        x =x+leng+(leng/2)
        h_writer(leng,x,y,each["hsn"],pdf)
        
        x =x+leng
        h_writer(leng+(leng/2),x,y,each["cost"],pdf)
        
        x =x+leng+(leng/2)
        h_writer(leng,x,y,each["qty"],pdf)
        
        x =x+leng
        h_writer(leng+(leng/2),x,y,each["t_cost"],pdf)
        
        x =x+leng+(leng/2)
        h_writer(leng,x,y,each["gst"],pdf)
        
        x = x+leng
        h_writer(leng+(leng/2),x,y,each["g_cost"],pdf)

        

    y = 126.0
    for idx,each in enumerate(tdata):
        leng,x,y=[20.1,10.0,y+5] 
        b_writer(leng/2,x,y,each["id"],pdf)
        
        x =x+leng/2
        b_writer(leng+(leng/2),x,y,each["desc"],pdf)
        
        x =x+leng+(leng/2)
        b_writer(leng,x,y,each["hsn"],pdf)
        
        x =x+leng
        b_writer(leng+(leng/2),x,y,each["cost"],pdf)
        
        x =x+leng+(leng/2)
        b_writer(leng,x,y,each["qty"],pdf)
        
        x =x+leng
        b_writer(leng+(leng/2),x,y,each["t_cost"],pdf)
        
        x =x+leng+(leng/2)
        b_writer(leng,x,y,each["gst"],pdf)
        
        x = x+leng
        b_writer(leng+(leng/2),x,y,each["g_cost"],pdf)

    y = y + 10
    pdf.line(10.0,y,80.0,y)
    pdf.set_xy(80.0,y-2)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=40, h=5.0, align='C', txt="End of Line items",border=0)
    pdf.line(120.0,y,200.0,y)

    l = 0
    m = 0
    y+=3
    yy =y
    pdf.set_xy(10.0,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=90, h=5.0, align='L', txt="Included in the Quote",border=0)

    for each in inclusive:
        y+=5
        pdf.set_xy(15.0,y)
        pdf.set_font('Montserrat Regular',"", 9)
        pdf.multi_cell(w=80, h=5.0, align='L', txt=str(each),border=0)
        l = y
        
    y = yy
    pdf.set_xy(105.0,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=80, h=5.0, align='L', txt="Excluded in the Quote",border=0)

    for each in exclusive:
        y+=5
        pdf.set_xy(110.0,y)
        pdf.set_font('Montserrat Regular',"", 9)
        pdf.multi_cell(w=80, h=5.0, align='L', txt=str(each),border=0)
        m = y
    if m > l:
        y = m
    else:
        y = l
        
    y=y+10
    pdf.line(10.0,y,200.0,y)






    y+=3
    pdf.set_xy(10.0,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=190, h=5.0, align='L', txt="Terms / Conditions",border=0)



    for each in remarks:
        y+=5
        pdf.set_xy(15.0,y)
        pdf.set_font('Montserrat Regular',"", 9)
        pdf.multi_cell(w=190, h=5.0, align='L', txt=str(each),border=0)


    y+=10
    pdf.line(10.0,y,200.0,y)

    y+=5
    pdf.set_xy(100.0,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=100, h=5.0, align='C', txt="Melvin & Venfra Innovative industrial Solutions",border=0)

    y+=5
    pdf.set_xy(100.0,y)
    pdf.set_font('Montserrat Bold',"", 9)
    pdf.multi_cell(w=100, h=5.0, align='C', txt="Melvin Paul Miki",border=0)


    y+=10
    pdf.line(10.0,y,200.0,280)


    pdf.output(_quote_id+'.pdf','F')