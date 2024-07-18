import React, {useState} from "react";
import styled from "styled-components";

const Container = styled.div`
    display: flex;
    width: 100%;
    height: 80px
`
const SelectedButton = styled.div`
    cursor: pointer;
    user-select: none;
    padding: 4px 8px;
    margin: auto auto;
    background-color: var(--grey);
    color: var(--black);
    border-radius: 8px;
`;

const DefaultButton = styled(SelectedButton)`
    background-color: var(--tertiary-color);
    color: var(--on-tertiary-color);
`
const Expand = styled.div`
    flex: 1;

`


interface ButtonProps {
    pageSelected: string,
    name: string,
    children: React.ReactNode,
    onClick?: (name: string) => void
}

const Button: React.FC<ButtonProps> = ({ pageSelected, name, children, onClick }) => {


    return name === pageSelected ? <DefaultButton onClick={() => onClick ? onClick(name): undefined}>{children}</DefaultButton>
        : <SelectedButton onClick={() => onClick ? onClick(name): undefined}>{children}</SelectedButton>;
}


const MainNavBar: React.FC = () => {
    const [pageSelected, setPageSelected] = useState("Vagas")

    function handleClick(name: string) {
        setPageSelected(name)
    }
    return (
        <Container>
            {/* Todo: Trampof Logo */}
            
            <Button pageSelected={pageSelected} name="Vagas" onClick={handleClick} >Vagas</Button>
            <Button pageSelected={pageSelected} name="Aplicativos" onClick={handleClick}>Aplicativos</Button>
            
            <Expand />
            {/* Todo: Config and log out buttons */}
        </Container>
    )
}

export default MainNavBar