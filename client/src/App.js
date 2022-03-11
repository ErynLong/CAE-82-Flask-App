import React, { useContext } from 'react';
import { Route, Routes } from 'react-router-dom';
import './App.css';
import AdminMenu from './components/AdminMenu';
import CheckOutSuccess from './components/CheckOutSuccess';
import Item from './components/Item';
import NavBar from './components/NavBar';
import RequireAdmin from './components/RequireAdmin';
import SnackBar from './components/SnackBar';
import { AppContext } from './context/AppContext';
import AdminCategory from './views/AdminCategory';
import AdminItem from './views/AdminItems';
import CartPage from './views/CartPage';
import Login from './views/Login';
import Logout from './views/Logout';
import ShopBrowser from './views/ShopBrowser';
import Box from '@mui/material/Box';

const HomePage=()=>{return(<h1>Welcome to the show!</h1>)}


function App() {
  const {user}=useContext(AppContext)

  return (
    <>
      <SnackBar/>
      <NavBar>
      <Box sx={{minHeight:'90vh'}}>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/cart" element={<CartPage/>}/>
          <Route path="/cart/:canceled" element={<CartPage/>}/>

          <Route path="/shop" element={<ShopBrowser/>}/>
          <Route path="/shop/:itemId" element={<Item />}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/logout" element={<Logout/>}/>
          <Route path="/checkoutsuccess" element={<CheckOutSuccess/>}/>
          <Route path="/admincat" element={
          <RequireAdmin redirectTo={"/login"}>
            <AdminCategory/>
          </RequireAdmin>
        }/>
        
          <Route path="/adminitem" element={<RequireAdmin redirectTo={"/login"}><AdminItem/></RequireAdmin>}/>
        </Routes>

        
</Box>
        {user?.is_admin?<AdminMenu/>:''}
      </NavBar>
    </>
  );
}

export default App;


