import React from "react";
import styled from "styled-components";

import Layout from "../../layout";
import DashboardVerticalMenu from "../../components/DashboardVerticalMenu";

const jobs: Array<string> = ["Django", "React", "Nest.js", "FastAPI", "React Native"];

const DashboardContainer = styled.div`
    display: grid;
    grid-template-columns: 0fr 1fr;
`

const Dashboard: React.FC = () => {

    return (
        <Layout>
            <DashboardContainer>
                <DashboardVerticalMenu jobs={jobs}/>
                <p>Dashboard page</p>
            </DashboardContainer>
        </Layout>
    )
}

export default Dashboard;