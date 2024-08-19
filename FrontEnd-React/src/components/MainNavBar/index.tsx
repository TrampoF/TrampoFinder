import React, { useState } from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";

const Container = styled.div`
    display: flex;
    align-items: center;
    width: 100%;
    height: 80px;
    padding: 0 20px;
`;

const SelectedButton = styled.div`
    cursor: pointer;
    user-select: none;
    padding: 4px 8px;
    margin: auto 8px;
    background-color: var(--grey);
    color: var(--black);
    border-radius: 8px;
`;

const DefaultButton = styled(SelectedButton)`
    background-color: var(--tertiary-color);
    color: var(--on-tertiary-color);
`;

const Expand = styled.div`
    flex: 1;
`;

const LogoContainer = styled(Link)`
    display: flex;
    align-items: center;
    margin-right: 20px;
`;

const Logo = styled.img`
    height: 60px;
    width: auto;
`;

const StyledLink = styled(Link)`
    margin: 0 15px;
    padding: 4px 8px;
    font-size: 25px;
    color: var(--link-color);
    text-decoration: none;
    border-radius: 8px;
    background-color: var(--link-bg-color);
    transition: background-color 0.3s, color 0.3s;

    &:hover {
        background-color: var(--link-hover-bg-color);
        color: var(--link-hover-color);
    }
`;

interface ButtonProps {
    pageSelected: string;
    name: string;
    children: React.ReactNode;
    onClick?: (name: string) => void;
    to: string;
}

const Button: React.FC<ButtonProps> = ({ pageSelected, name, children, onClick, to }) => {
    return name === pageSelected ? (
        <DefaultButton as={Link} to={to} onClick={() => (onClick ? onClick(name) : undefined)}>
            {children}
        </DefaultButton>
    ) : (
        <SelectedButton as={Link} to={to} onClick={() => (onClick ? onClick(name) : undefined)}>
            {children}
        </SelectedButton>
    );
};

const MainNavBar: React.FC = () => {
    const [pageSelected, setPageSelected] = useState("Vagas");

    function handleClick(name: string) {
        setPageSelected(name);
    }

    return (
        <Container>
            <LogoContainer to="/">
                <Logo src="/images/trampofinder.svg" alt="Logo" />
            </LogoContainer>
            <Button pageSelected={pageSelected} name="Vagas" onClick={handleClick} to="/app">
                Vagas
            </Button>
            <Button pageSelected={pageSelected} name="Aplicativos" onClick={handleClick} to="/aplicativos">
                Aplicativos
            </Button>
            <Expand />
            <StyledLink to="/login">Login</StyledLink>
            <StyledLink to="/cadastro">Cadastro</StyledLink>
        </Container>
    );
};

export default MainNavBar;
