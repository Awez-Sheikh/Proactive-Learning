import { createContext } from "react";

const studentData = {
    name: "Awez Sheikh",
    age: 19,
    sex: "M",
    address: "Urban",
    famsize: "GT3",
    Pstatus: "T",
    Medu: 3,
    Fedu: 2,
    Mjob: "Teacher",
    Fjob: "Other",
    reason: "other",
    guardian: "father",
    traveltime: "2",
    studytime: "2",
    failures: "0",
    schoolsup: "1",
    famsup: "1",
    paid: 0,
    activities: 1,
    nursery: 1,
    higher: 1,
    internet: 1,
    romantic: 1,
    famrel: 1,
    freetime: 1,
    goout: 1,
    Dalc: 1,
    Walc: 1,
    health: 1,
    absences: 4,
    G1: 0,
    G2: 55,
    G3: 55,
    G4: 0,
    G5: 0,
    G6: 0,
    G7: 0,
    Grade_8_Marks: 80,
    Grade_9_Marks: 78,
    Grade_10_Marks: 85,
    Grade_11_Marks: 82,
    Grade_12_Marks: 90,
    course: "CSE",
    semester: "6",
  };



  export const StudentDataContext = createContext();
  export default studentData;


