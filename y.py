import re

data = """
Create or replace the values -- hsbdjfbwj hbdjwhbdhwb
--the maisn ddatas for the loop
The value is defined in aparticular way
string main attcahed, variables , etc
/* sdwqbwsdhqjbjbdjq qbakjdhqkhdkq*/
aadvqwghvdhgqwvhgdvqwhgdvqwhjdjdq
hqvdghqvwhgdvqwhjgdjqh
/*****
dqwgwdjq
dghqwvdjvq
***
***
dhqvbdjqj
GHDVHGQWWDQ
*/
the madsis data which has for the values /* vdhgqvjdvqj*/ cwhgdvhq
gsvsgdwgdw
end
end;
"""

print("With Comments Data\n",data)

removed_data_comment1=re.sub(r'\--.+','',data)
removed_data_comment2=re.sub(r'\/\*([\s\S]*?)\*/','',removed_data_comment1)

print("Without comments Data\n",removed_data_comment2)
























