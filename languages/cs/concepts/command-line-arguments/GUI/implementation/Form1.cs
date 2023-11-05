using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Your_Project_Namespace
{
    public partial class MyForm : Form
    {
        public MyForm(string[] args)
        {
            // Class Constructor
            InitializeComponent();

            for (int i=0; i < args.Length; i++)
            {
                Console.WriteLine("{0} = {1}", i, args[i]);
            }
        }

        ~MyForm()
        {
            // Class Destructor
        }

        private void MyForm_Load(object sender, EventArgs e)
        {
            // On Form Page Load
        }
                    
        private void btnClickThis_Click(object sender, EventArgs e)
        {
            // On Button Click
            MessageBox.Show("My First WinForm Application");
        }
    }
}
