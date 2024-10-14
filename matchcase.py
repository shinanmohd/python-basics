#6 - august

# match_case.statement
'''match variable_name:
    case pattern 1:
        statement 1
    case pattern 2:
        statement 3'''

'''def weekday(day):
    match day:
        case 1:
            return 'monday'
        case 2:
            return 'tuesday'
print(weekday(1))
print(weekday(3))'''

#-----------------------------------------------------
'''
def access(user):
    match user:
        case "admin"|"manager":
            return "user is manager or admin"
        case "Guest":
            return "user is a guest"
        case "normal user":
            return "User is a normal user"
        case _:
            return "no one can access"
print(access("admin"))
'''
#------------------------------------------------------
'''
def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen","Lata"]))
'''
#--------------------------------------------------------
'''
def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))
'''























