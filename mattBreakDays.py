
# coding: utf-8

# In[43]:


def accessMattsWeek(day):
    '''Return the acivities Matt did over break by inputting day of the week'''
    mattsWeek = {
    'monday':'Work',
    'tuesday':'Work',
    'wednesday':'Work',
    'thursday':'Work',
    'friday':'Ate dinner at Piada',
    'saturday':'Drove to Elizabeth for Easter with grandparents',
    'sunday':'Drove to Cranberry for Easter brunch, then Penn Hills for Easter dinner',
}
    if day in mattsWeek:
        return mattsWeek[day]
    else:
        return "day not found"
    
whatday = input('')
print(accessMattsWeek(whatday.lower()))

