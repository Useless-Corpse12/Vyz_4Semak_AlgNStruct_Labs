using SotoviyOperator.BackLayer.Sim_Cards;
using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SotoviyOperator.BackLayer
{
    internal class RngAddition
    {

        private static readonly Random _rnd = new Random();


        //Имена
        private static readonly char[] Vowels = { 'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я' };
        private static readonly char[] Consonants = { 'б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ' };

        private static readonly string[,] SurnameEndings = {
        { "ов", "ова" },
        { "ин", "ина" },
        { "их", "их" }, 
        { "ский", "ская" }
        };

        private static readonly string[,] NameEndings = {
        { "ев", "ева" },
        { "ов", "ова" },
        { "ий", "ия" },
        { "ан", "ана" }
        };

        private static readonly string[,] PatronymicEndings = {
        { "евич", "евна" },
        { "ович", "овна" },
        { "ич", "ична" }
        };

        public static string GenerateFam(bool isMale)
        {
            return GenerateSyllableRoot(1, 4) + (isMale ? SurnameEndings[_rnd.Next(4), 0] : SurnameEndings[_rnd.Next(4), 1]); ;
        }

        public static string GenerateNam(bool isMale)
        {
            return GenerateSyllableRoot(1, 3) + (isMale ? NameEndings[_rnd.Next(4), 0] : NameEndings[_rnd.Next(4), 1]);
        }

        public static string GenerateFNam(bool isMale)
        {
            return GenerateNam(true).Substring(0,-2) + (isMale ? PatronymicEndings[_rnd.Next(3), 0] : PatronymicEndings[_rnd.Next(3), 1]);
        }

        public static string GenerateFullName(bool isMale)
        {

            return $"{Capitalize(GenerateFam(isMale))} {Capitalize(GenerateNam(isMale))} {Capitalize(GenerateFNam(isMale))}";
        }
        public static string GenerateFullName()
        {
            bool isMale = _rnd.Next(2)==1 ? true : false;
            return $"{Capitalize(GenerateFam(isMale))} {Capitalize(GenerateNam(isMale))} {Capitalize(GenerateFNam(isMale))}";
        }

        private static string GenerateSyllableRoot(int minSyllables, int maxSyllables)
        {
            int count = _rnd.Next(minSyllables, maxSyllables + 1);
            var sb = new StringBuilder();

            for (int i = 0; i < count; i++)
            {
                sb.Append(GetRandom(Vowels));
                sb.Append(GetRandom(Consonants));
            }
            return sb.ToString();
        }

        private static T GetRandom<T>(T[] array)
        {
            return array[_rnd.Next(array.Length)];
        }

        private static string Capitalize(string str)
        {
            if (string.IsNullOrEmpty(str)) return str;
            return char.ToUpper(str[0]) + str.Substring(1);
        }

        //Адреса
        private static readonly string[] CitySuffixes = { "град", "город", "бург", "ск", "виль", "поль" };

        private static readonly string[] StreetTypesMale = { "пер.", "ул.", "пр-т", "бульвар", "проспект" };
        private static readonly string[] StreetTypesFemale = { "пер.", "ул.", "аллея", "набережная" };
        private static readonly string[][] AllStreetsType = new string[][] {StreetTypesMale, StreetTypesFemale};
        public static string GenerateCity()
        {
            if (_rnd.Next(2)==1)
            {
                return GenerateNam(false);
            }
            else
            {
                return GenerateSyllableRoot(1,4) + GetRandom(CitySuffixes);
            }
        }

        public static string GenerateStreet()
        {
            int dick_count= _rnd.Next(2);
            bool dick_factor = dick_count > 0;
            return GetRandom(AllStreetsType[dick_count]) + GetSurnameInGenitive(GenerateNam(dick_factor));
        }

        private static string GetSurnameInGenitive(string lastName)
        {
            if (string.IsNullOrEmpty(lastName)) return "Центральная";

            string lowerLast = lastName.ToLower();

            if (lowerLast.EndsWith("ий") || lowerLast.EndsWith("ый"))
                {return lastName.Substring(0, lastName.Length - 2) + "ого";}
            else if (lowerLast.EndsWith("ова") || lowerLast.EndsWith("ева") || lowerLast.EndsWith("ина")) 
                {return lastName.Substring(0, lastName.Length - 1) + "ой";}
            else if (lowerLast.EndsWith("ская"))
                {return lastName.Substring(0, lastName.Length - 2) + "ой";}
            else if (lowerLast.EndsWith("их"))
                {return lastName;}
            return lastName + "а";
        }

        public static string GenerateFullAdress()
        {
            return $"г.{GenerateCity()} {GenerateStreet()} д.{_rnd.Next(1,199)}";
        }

        public static int GenerateClientBYear()
        {
            return DateTime.Now.Year - _rnd.Next(109)-14;//Самый старый человек 123 года
        }

        public static string GeneratePassNum()
        {
            return _rnd.Next(1000, 9999).ToString() + '-' + _rnd.Next(100000, 999999);
        }


        public static string GeneratePassA(int BDate)
        {
            return "ГУ МВД по "+ GenerateFullAdress() + (DateTime.Now - DateTime.Dat)
        }


    }
}
