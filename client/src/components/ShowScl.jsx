import axios from 'axios';
import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


const ShowScl = () => {
    const [schools, setSchools] = useState([]);
    const [classes, setClasses] = useState([]);
    const [Assessment, setAssessment] = useState([]);
    const [Answers, setAnswers] = useState([]);
    const [Awards, setAwards] = useState([]);
    const [Student, setStudent] = useState([]);
    const [Subject, setSubject] = useState([]);
    const [Category, setCategory] = useState([]);
    const [Summery, setSummery] = useState([]);

    const baseURL = 'http://localhost:8000';

    const getSchools = async () => {
        try {
            const response = await axios.get(`${baseURL}/school/`);
            setSchools(response.data);
        } catch (error) {
            console.error("Error fetching school data:", error);
        }
    }

    useEffect(() => {
        getSchools();
    }, []);

    const getClasses = async () => {
        try {
            const response = await axios.get(`${baseURL}/class/`);
            setClasses(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getClasses();
    }, []);

    const getAssessment = async () => {
        try {
            const response = await axios.get(`${baseURL}/Assessment/`);
            setAssessment(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getAssessment();
    }, []);


    const getAnswers = async () => {
        try {
            const response = await axios.get(`${baseURL}/Answers/`);
            setAnswers(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getAnswers();
    }, []);

    const getAwards = async () => {
        try {
            const response = await axios.get(`${baseURL}/Awards/`);
            setAwards(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getAwards();
    }, []);


    const getStudent = async () => {
        try {
            const response = await axios.get(`${baseURL}/Student/`);
            setStudent(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getStudent();
    }, []);


    const getSubject = async () => {
        try {
            const response = await axios.get(`${baseURL}/Subject/`);
            setSubject(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getSubject();
    }, []);


    const getCategory= async () => {
        try {
            const response = await axios.get(`${baseURL}/Category/`);
            setCategory(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getCategory();
    }, []);

    const getSummery= async () => {
        try {
            const response = await axios.get(`${baseURL}/Summery/`);
            setSummery(response.data);
        } catch (error) {
            console.error("Error fetching class data:", error);
        }
    }

    useEffect(() => {
        getSummery();
    }, []);

    return (
        <div>
           
            <h1>Django Project</h1>
<br></br>

                 <Container>
                 <Row>
        <Col xs={6} md={4}>
            <h3>School Table</h3>
            <Table striped>
                <thead>
                    <tr>
                        <th>School ID</th>
                        <th>School Name</th>
                    </tr>
                </thead>
                <tbody>
                    {schools.map((school, index) => (
                        <tr key={index}>
                            <td>{school.School_Id}</td>
                            <td>{school.Sch_Name}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            </Col>
            <Col xs={6} md={4}>
            <h3>Class Table</h3>
            <div style={{ height: '300px', overflow: 'auto' }}>
    <Table striped>
        <thead>
            <tr>
                <th>Class ID</th>
                <th>Class Name</th>
            </tr>
        </thead>
        <tbody>
            {classes.map((classItem, index) => (
                <tr key={index}>
                    <td>{classItem.Class_Id}</td>
                    <td>{classItem.Class}</td>
                </tr>
            ))}
        </tbody>
    </Table>
</div>
</Col>
<Col xs={6} md={4}>
<h3>Assessment Table</h3>
            <div style={{ height: '300px', overflow: 'auto' }}>
    <Table striped>
        <thead>
            <tr>
                <th>Assessment ID</th>
                <th>Assessment Area</th>
            </tr>
        </thead>
        <tbody>
            {Assessment.map((Assessment, index) => (
                <tr key={index}>
                    <td>{Assessment.Assessment_Areas_Id}</td>
                    <td>{Assessment.Assessment_Area}</td>
                </tr>
            ))}
        </tbody>
    </Table>



</div>
</Col>
</Row>
<hr></hr>

<Row>
        <Col xs={6} md={4}>
            <h3>Answers Table</h3>
            <Table striped>
                <thead>
                    <tr>
                        <th>Answer Id</th>
                        <th>Answer</th>
                    </tr>
                </thead>
                <tbody>
                    {Answers.map((Answers, index) => (
                        <tr key={index}>
                            <td>{Answers.Answer_Id}</td>
                            <td>{Answers.Answer}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            </Col>
            <Col xs={6} md={4}>
            <h3>Awards Table</h3>
            <div style={{ height: '300px', overflow: 'auto' }}>
    <Table striped>
        <thead>
            <tr>
                <th>Award Id</th>
                <th>Award</th>
            </tr>
        </thead>
        <tbody>
            {Awards.map((Awards, index) => (
                <tr key={index}>
                    <td>{Awards.Award_Id}</td>
                    <td>{Awards.Award}</td>
                </tr>
            ))}
        </tbody>
    </Table>
</div>
</Col>
<Col xs={6} md={4}>
<h3>Student Table</h3>
            <div style={{ height: '300px', overflow: 'auto' }}>
    <Table striped>
        <thead>
            <tr>
                <th>Student Id</th>
                <th>Full Name</th>
            </tr>
        </thead>
        <tbody>
            {Student.map((Student, index) => (
                <tr key={index}>
                    <td>{Student.Student_Id}</td>
                    <td>{Student.Fullname}</td>
                </tr>
            ))}
        </tbody>
    </Table>



</div>
</Col>
</Row>

<hr></hr>

<Row>
        <Col xs={6}>
            <h3>Subject Table</h3>
            <Table striped>
                <thead>
                    <tr>
                        <th>Subject Id</th>
                        <th>Subject</th>
                    </tr>
                </thead>
                <tbody>
                    {Subject.map((Subject, index) => (
                        <tr key={index}>
                            <td>{Subject.Subject_Id}</td>
                            <td>{Subject.Subject}</td>
                            <td>{Subject.Subject_score}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            </Col>
            <Col xs={6}>
            <h3>Category Table</h3>
            <div style={{ height: '300px', overflow: 'auto' }}>
    <Table striped>
        <thead>
            <tr>
                <th>Category Id</th>
                <th>Category</th>
            </tr>
        </thead>
        <tbody>
            {Category.map((Category, index) => (
                <tr key={index}>
                    <td>{Category.Category_Id}</td>
                    <td>{Category.Category}</td>
                </tr>
            ))}
        </tbody>
    </Table>
</div>
</Col>

</Row>

<hr></hr>
<Row>
        <Col xs={12}>
        <div style={{ overflowX: 'auto' }}>
            <h3>Summery Table</h3>
            <Table striped>
                <thead>
                    <tr>
                        <th>School Id</th>
                        <th>Student Id</th>
                        <th>Class Id</th>
                        <th>Subject Id</th>
                        <th>Category Id</th>
                        <th>Assessment Areas Id</th>
                        <th>Year level name</th>
                        <th>Answer Id</th>
                        <th>Correct Answer</th>
                    
                        <th>Correct answer percentage per class</th>
                        <th>Sydney participants</th>

                        <th>Sydney percentile</th>
                        <th>Student score</th>
                        <th>Participant</th>

                        <th>Award Id</th>
                
                    </tr>
                </thead>
                <tbody>
                    {Summery.map((Summery, index) => (
                        <tr key={index}>
                            <td>{Summery.School_Id}</td>
                            <td>{Summery.Student_Id}</td>
                            <td>{Summery.Class_Id}</td>
                            <td>{Summery.Subject_Id}</td>
                            <td>{Summery.Category_Id}</td>
                            <td>{Summery.Assessment_areas_Id}</td>
                            <td>{Summery.Year_level_name}</td>
                            <td>{Summery.Answer_Id}</td>
                            <td>{Summery.Correct_Answer}</td>
                            <td>{Summery.correct_answer_percentage_per_class}</td>
                            <td>{Summery.sydney_participants}</td>
                            <td>{Summery.sydney_percentile}</td>

                            <td>{Summery.student_score}</td>
                            <td>{Summery.participant}</td>

                            
                            <td>{Summery.Award_Id}</td>
                           
                        </tr>
                    ))}
                </tbody>
            </Table>
            </div>
            </Col>
 

</Row>




</Container>
        </div>

    
    );
};

export default ShowScl;
