using System;
using System.Collections.Generic;

namespace SotoviyOperator.BackLayer.Sim_Cards
{
    internal class HashCell
    {
        public SimC Data;
        public bool IsDeleted;
    }
    internal class HashTable
    {
        private const int _TABLE_SIZE = 1009; //1009 - Простое число - это важно!
        private readonly HashCell[] _table = new HashCell[_TABLE_SIZE];
        public static int JHash1(string key) //Хеш-функция 1
        {
            int hash = 0;
            foreach (char ch in key)
                hash = (hash * 67 + ch) % _TABLE_SIZE; // 67 - Тоже простое число - это тоже важно!

            //Код создающий "Эффект лавины" взятый из murmur3, решающий вопрос, когда "соседние" ключи типа "aaa" и "aab" образуют "соседние" хеши типо X+n(напр 552) и X+2n(напр 553)... и т.д
            hash ^= (hash >> 16); 
            hash *= -2047273877;
            hash ^= (hash >> 13);
            hash *= -1028256203;
            hash ^= (hash >> 16);
            return hash % _TABLE_SIZE;
        }

        public static int JHash2(string key)
        {
            int hash = 0;
            foreach (char ch in key)
                hash = (hash * 87 + ch) % (_TABLE_SIZE-2); // 87 - Тоже простое число - это тоже важно!

            hash ^= (hash >> 16);
            hash *= -2047273877;
            hash ^= (hash >> 13);
            hash *= -1028256203;
            hash ^= (hash >> 16);
            return (hash % (_TABLE_SIZE-1))+1;
        }

        public void Add(SimC sim)
        {
            int start = JHash1(sim.Number);
            int step = JHash2(sim.Number);

            for (int i = 0; i < _TABLE_SIZE; i++)
            {
                int idx = (start + i * step) % _TABLE_SIZE;

                // Свободно -> кладём
                if (_table[idx] == null || _table[idx].IsDeleted)
                {
                    _table[idx] = new HashCell { Data = sim, IsDeleted = false };
                    return;
                }

                // Ключ есть -> обновляем
                if (_table[idx].Data.Number == sim.Number)
                {
                    _table[idx].Data = sim;
                    return;
                }
            }
            throw new InvalidOperationException("Хеш-таблица переполнена.");
        }

        public SimC Search(string number)
        {
            int start = JHash1(number);
            int step = JHash2(number);

            for (int i = 0; i < _TABLE_SIZE; i++)
            {
                int idx = (start + i * step) % _TABLE_SIZE;

                if (_table[idx] == null) return null; 
                if (_table[idx].IsDeleted) continue; 
                if (_table[idx].Data.Number == number) return _table[idx].Data;
            }
            return null;
        }

        public bool Remove(string number)
        {
            int start = JHash1(number);
            int step = JHash2(number);

            for (int i = 0; i < _TABLE_SIZE; i++)
            {
                int idx = (start + i * step) % _TABLE_SIZE;

                if (_table[idx] == null) return false;
                if (!_table[idx].IsDeleted && _table[idx].Data.Number == number)
                {
                    _table[idx].IsDeleted = true;
                    return true;
                }
            }
            return false;
        }

        public List<SimC> GetAll()
        {
            var list = new List<SimC>(_TABLE_SIZE);
            foreach (var cell in _table)
                if (cell != null && !cell.IsDeleted) list.Add(cell.Data);
            return list;
        }


    }
}
