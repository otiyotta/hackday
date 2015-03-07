#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
  my_point =[
             (35.624093586339576, 139.60086822509766), 
             (35.59506483918009, 139.5754623413086),
             (35.581942623124036, 139.56584930419922),
             (35.543401137387335, 139.53907012939453),
             (35.55010533588551, 139.54593658447266),
             (35.54312178361944, 139.53907012939453),
             (35.54004882795015, 139.5366668701172),
             (35.530829254531724, 139.52327728271484),
             (35.527476419681335, 139.51229095458984),
             (35.51881428123057, 139.50267791748047),
             (35.50008969167118, 139.4776153564453)
            ]
  print_mypoint(my_point)
  print_subpoint(my_point)
  
def print_mypoint(my_point):
  for i in my_point:
    print '''
 		data.push({position: new google.maps.LatLng(%s, %s),
                      imgpath: './pic/red-dot.png',
                      content: 'りんご' + '<video controls="" style="width:100px;height:100px;" >' +
 					'<source src="./movie/hogehoge.mp4" type="video/mp4;">' +
 					'</video>'});
          ''' %(i[0],i[1])

def print_subpoint(my_point):
  first_flag=0
  terms=['ゴリラ','らっぱ','ぱんだ','団子','ごま']
  for i in my_point:
    now=i

    if first_flag==0:
      first_flag=1
      pre=i
      continue


    h_point, w_point = subpoint(pre,now,len(terms))
    for n in range(len(terms)):
      print '''
			data.push({position: new google.maps.LatLng(%s, %s),
                             imgpath: './pic/star.png',
                             content: '%s' + '<video controls="" style="width:100px;height:100px;" >' +
							'<source src="./movie/hogehoge.mp4" type="video/mp4;">' +
							'</video>'});
              ''' %(h_point[n] ,w_point[n], terms[n])
    pre=now

def subpoint(pre,now,n):
  h_sub =min(pre[0],now[0])- max(pre[0],now[0])
  w_sub =min(pre[1],now[1])- max(pre[1],now[1])

  h_step=h_sub/(n+1)
  w_step=w_sub/(n+1)

  h_point=[]
  for h in range(n):
    h_point.append(max(pre[0],now[0])+(h_step*(1+h)))

  w_point=[]
  for w in range(n):
    w_point.append(max(pre[1],now[1])+(w_step*(1+w)))

  #print h, h_point, w_point
  return h_point, w_point
  
if __name__ == '__main__':
  main()




