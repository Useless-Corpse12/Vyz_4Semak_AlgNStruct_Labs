using System;
using System.Collections.Generic;

namespace SotoviyOperator.BackLayer.Clients
{
    public class AVLNode
    {
        public Client Data { get; set; }
        public AVLNode Left { get; set; }
        public AVLNode Right { get; set; }
        public int Height { get; set; }
        public AVLNode(Client client)
        {
            Data = client;
            Height = 1;
        }
    }

    public class AVLTree
    {
        private AVLNode root;

        public void Insert(Client client) => root = InsertRecursive(root, client);

        private AVLNode InsertRecursive(AVLNode node, Client client)
        {
            if (node == null)
                return new AVLNode(client);

            int cmp = string.Compare(client.Passport, node.Data.Passport);

            if (cmp < 0)
                node.Left = InsertRecursive(node.Left, client);
            else if (cmp > 0)
                node.Right = InsertRecursive(node.Right, client);
            else
                return node;

            return Rebalance(node);
        }

        private int GetHeight(AVLNode node) => node == null ? 0 : node.Height;
        private int GetBalance(AVLNode node) => node == null ? 0 : GetHeight(node.Left) - GetHeight(node.Right);

        public Client Search(string passport)
        {
            return SearchRecursive(root, passport);
        }

        private Client SearchRecursive(AVLNode node, string passport)
        {
            if (node == null) return null;

            int cmp = string.Compare(passport, node.Data.Passport);

            if (cmp == 0) return node.Data;

            return cmp < 0 ? SearchRecursive(node.Left, passport) : SearchRecursive(node.Right, passport);
        }

        public void Delete(string passport) => root = DeleteNode(root, passport);

        private AVLNode DeleteNode(AVLNode node, string passport)
        {
            if (node == null)
                return null;
            int cmp = string.Compare(passport, node.Data.Passport);

            if (cmp < 0)
                node.Left = DeleteNode(node.Left, passport);
            else if (cmp > 0)
                node.Right = DeleteNode(node.Right, passport);
            else
            {
                // Узел найден
                if (node.Left == null || node.Right == null)
                {
                    // 0 или 1 ребёнок
                    AVLNode temp = node.Left ?? node.Right;
                    if (temp == null)
                    {
                        temp = node;
                        node = null;
                    }
                    else
                    {
                        node = temp;
                    }
                }
                else
                {
                    // 2 ребёнка: находим минимальный в правом поддереве
                    AVLNode temp = GetMin(node.Right);
                    node.Data = temp.Data;
                    node.Right = DeleteNode(node.Right, temp.Data.Passport);
                }
            }

            if (node == null)
                return null;


            return Rebalance(node);
        }

        private AVLNode Rebalance(AVLNode node)
        {
            node.Height = 1 + Math.Max(GetHeight(node.Left), GetHeight(node.Right));
            int balance = GetBalance(node);

            // LL
            if (balance > 1 && GetBalance(node.Left) >= 0)
                return RotateRight(node);
            // RR
            if (balance < -1 && GetBalance(node.Right) <= 0)
                return RotateLeft(node);
            // LR
            if (balance > 1 && GetBalance(node.Left) < 0)
            {
                node.Left = RotateLeft(node.Left);
                return RotateRight(node);
            }
            // RL
            if (balance < -1 && GetBalance(node.Right) > 0)
            {
                node.Right = RotateRight(node.Right);
                return RotateLeft(node);
            }

            return node;
        }

        private AVLNode RotateRight(AVLNode y)
        {
            AVLNode x = y.Left;
            AVLNode T2 = x.Right;

            x.Right = y;
            y.Left = T2;

            y.Height = 1 + Math.Max(GetHeight(y.Left), GetHeight(y.Right));
            x.Height = 1 + Math.Max(GetHeight(x.Left), GetHeight(x.Right));

            return x;
        }

        private AVLNode RotateLeft(AVLNode x)
        {
            AVLNode y = x.Right;
            AVLNode T2 = y.Left;

            y.Left = x;
            x.Right = T2;

            x.Height = 1 + Math.Max(GetHeight(x.Left), GetHeight(x.Right));
            y.Height = 1 + Math.Max(GetHeight(y.Left), GetHeight(y.Right));

            return y;
        }

        private AVLNode GetMin(AVLNode node)
        {
            AVLNode current = node;
            while (current.Left != null)
                current = current.Left;
            return current;
        }

        public List<Client> InOrder()
        {
            var result = new List<Client>();
            InOrderRec(root, result);
            return result;
        }

        private void InOrderRec(AVLNode node, List<Client> result)
        {
            if (node != null)
            {
                InOrderRec(node.Left, result);
                result.Add(node.Data);
                InOrderRec(node.Right, result);
            }
        }

        public List<Client> PreOrder()
        {
            var result = new List<Client>();
            PreOrderRec(root, result);
            return result;
        }

        private void PreOrderRec(AVLNode node, List<Client> list)
        {
            if (node == null) return;

            list.Add(node.Data);
            PreOrderRec(node.Left, list);
            PreOrderRec(node.Right, list);
        }
    }
}
