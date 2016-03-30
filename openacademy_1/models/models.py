class Course(models.Model):
    _name = 'openacademy.course'
responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
Tambien tenemos que modificar el archivo xml demo.xml, añadiendo el siguiente <record>:

<record model="openacademy.course" id="course0">
            <field name="name">Course 0</field>
            <field name="description">Course 0's description

Can have multiple lines
            </field>
        </record>
        <record model="openacademy.course" id="course1">
            <field name="name">Course 1</field>
            <!-- no description for this one -->
        </record>
        <record model="openacademy.course" id="course2">
            <field name="name">Course 2</field>
            <field name="description">Course 2's description</field>
        </record>
class Session(models.Model):
    _name = 'openacademy.session'
instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")