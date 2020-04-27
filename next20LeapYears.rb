# I haven't used ruby in forever, 
# but this is the same as my initial python logic.
# This prints the next 20 leap years.

for n in 2021..2105 do
    if n % 4 == 0
        if n % 100 != 0 || n % 400 == 1
            puts n
        end
    end
end