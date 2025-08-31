// MainLayout.tsx

import { Outlet } from "react-router-dom";
const MainLayout = () => {
    return (
        <div className="relative flex h-screen bg-white dark:bg-black">
            <h1 className="text-red-400">Luma</h1>
            <ul>
                <li>FYP</li>
                <li>Explore</li>
                <li>Live</li>
                <li>Message</li>
            </ul>
            <button>Logout</button>
            <main className="relative md:ml-60 flex-1 overflow-y-auto main">
                <Outlet />
            </main>
        </div>
    );
};

export default MainLayout;