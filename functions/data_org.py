last_data = [{
    'location': 'googel',
    'data': [{'time': [12, 5], 'text': ['bla bla bla', '1234-']}]
}]

new_data = {
    'window_title': 'googel',
    'key_char': 'c',
    'time': ['12:05', '15/08/01']
}
# last_text = last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text'][
#             len(last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text']) - 1]
# print(last_text)
def moath_cklick():
    last_text = last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text'][
        len(last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text']) - 1]
    if last_text[len(last_text) - 1] != '-':
        last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text'][
            len(last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text']) - 1] += '-'

def data_orginaz(window_title, time, key_char):
    print(last_data)

    if last_data[len(last_data) - 1]['location'] != window_title:
        print('e')
        newd = {
            'location': window_title,
            'data': [{'times': time, 'text': [key_char]}]
        }
        last_data.append(newd)


    elif  last_data[len(last_data) - 1]['location'] == window_title:
        print('s')
        last_text = last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text'][
            len(last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text']) - 1]
        if last_text[len(last_text)-1] == '-':
            # הטקסט האחרון
            last_data[len(last_data)-1]['data'][len(last_data[len(last_data)-1]['data'])-1]['text'].append(key_char)
        else:
           last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text'][
               len(last_data[len(last_data) - 1]['data'][len(last_data[len(last_data) - 1]['data']) - 1]['text']) - 1] += key_char
           print(last_data)



    # print(last_data)

