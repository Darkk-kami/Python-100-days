from merger import Merger

merger = Merger()
    
for name in merger.name_list:
    letter_body = merger.letter_body()
    new_letter = letter_body.replace('[name]', f'{name}')
    merger.new_letter(name=name, letter=new_letter)



   











