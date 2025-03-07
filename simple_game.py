using System;

namespace Honors_Assignment
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter an item type (weapon, gem, loot):");
            string userInput = Console.ReadLine();

            if (userInput == "weapon")
            {
                Console.WriteLine("You have selected a weapon.");
                Console.WriteLine("Time to channel your inner warrior! Swing that sword like you mean it!");
            }
            else if (userInput == "gem")
            {
                Console.WriteLine("You have selected a gem.");
                Console.WriteLine("Shiny! This gem will make you sparkle brighter than a disco ball.");
            }
            else if (userInput == "loot")
            {
                Console.WriteLine("You have selected loot.");
                Console.WriteLine("Jackpot! Let's hope there's something more than just old socks in there.");
            }
            else
            {
                Console.WriteLine("Invalid item type.");
                Console.WriteLine("Oops! That doesn't seem right. Try entering a valid item type next time.");
            }
        }
    }
}

