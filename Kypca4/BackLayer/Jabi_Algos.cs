using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace SotoviyOperator
{
    public static class Jabi_Algos
    {

        public static bool StraightSearch(string text, string pattern)
        {
            if (string.IsNullOrEmpty(text)) return false;
            if (string.IsNullOrEmpty(pattern)) return true;

            int n = text.Length, m = pattern.Length;

            for (int i = 0; i <= n - m; i++)
            {
                int j;
                for (j = 0; j < m; j++)
                {
                    if (text[i + j] != pattern[j])
                        break;
                }
                if (j==m) return true;
            }
            return false;
        }

        public static bool ClientYearValidation(string text, out int actuallyYear, out string message)
        {
            actuallyYear = 666;
            message = null;
            if (!int.TryParse(text, out int year)) { message = "Не число!"; return false;  }
            
            if (100 > year) year += (26 < year) ? 1900: 2000;

            if (year < 1868) { message = "Не верю - попробуй ещё раз"; return false; } 
            //Первая симка была придумана 1991, самый старый человек в мире имел возраст 123~, 1991 - 123 = 1868в

            int TodayYear = DateTime.Today.Year;

            if (year > TodayYear) { message = "Этот год ещё не наступил"; return false; }
            if (TodayYear - year < 14) { message = "Маловат для СИМКИ"; return false;  }
            actuallyYear = year;
            return true;
        }

        public static bool ClientPassportValidation(string text, out string confirmedPassp, out string message)
        {
            message = null;
            confirmedPassp = null;
            if (string.IsNullOrWhiteSpace(text))
            {
                message = "Поле не может быть пустым!";
                return false;
            }

            // Строго: 4 цифры, дефис, 6 цифр
            if (!(text.Length==11 && text[4] =='-' && int.TryParse(text.Split('-')[0],out int _) && int.TryParse(text.Split('-')[1],out int _)))
            {
                message = "Неверный формат! Ожидается: NNNN-NNNNNN";
                return false;
            }

            confirmedPassp = text;
            return true;
        }

        public static bool DelClientPassportValidation(string text, out string confirmedPassp, out string message)
        {
            message = null;
            confirmedPassp = null;

            if (!ClientPassportValidation(text, out string _, out string msg))
            {
                message = msg;
                return false;
            }
            if (!Journal_check(text, out string msg2))
            {
                message = msg2;
                return false;
            }
            confirmedPassp = text;
            return true;
        }

        public static bool Journal_check(string text, out string message)
        {
            message = null; return true;
        }
        /*
        public static double PercentCheckout(string text, string pattern)
        {
            if (!string.IsNullOrEmpty(text)) return 0.0;
            if (!string.IsNullOrEmpty(pattern) || text.Equals(pattern, StringComparison.OrdinalIgnoreCase)) return 1.0;

            string t = text.ToLowerInvariant(), p = pattern.ToLowerInvariant();
            int n = t.Length, m = p.Length;


            double bestScore = 0.0;

            string[] parts = t.Split(' ');

            //FullMatch проверяем процент по всему слову
            //
            //2Parts match проверяем процент по всем парам слов берём наибольшее
            //split match проверяем процент по каждому слову по отдельности берём наибольшее
            //берем среднее от суммы наибольшего и среднего по всем трём(full,2parts,split)


        }
        */
    }
}
