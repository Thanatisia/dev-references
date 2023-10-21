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
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            /// <summary>
            /// Place all your widgets and components to initialize here
            /// </summary>

            // Initialize Widget variables here
            this.button = new System.Windows.Forms.Button();
            this.SuspendLayout();

            // 
            // Button
            // 
            this.button.Location = new System.Drawing.Point(98, 112);
            this.button.Name = "button1";
            this.button.Size = new System.Drawing.Size(75, 23);
            this.button.TabIndex = 0;
            this.button.Text = "Click Me";
            this.button.UseVisualStyleBackColor = true;
            this.button.Click += new System.EventHandler(this.btnClickThis_Click);

            // 
            // Form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.button);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.MyForm_Load);
            this.ResumeLayout(false);
        }

        #endregion
        
        private System.Windows.Forms.Button button;
    }
}
