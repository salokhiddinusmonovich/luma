import { Outlet } from "react-router-dom";
import { useTheme } from "@/hooks/useTheme";
import { Moon, Sun } from "lucide-react";


const MainLayout = () => {
    const { theme, toggleTheme }: ReturnType<typeof useTheme> = useTheme();

    return (
        <div className="relative flex h-screen bg-white dark:bg-black">
            <h1 className="text-red-400">Luma</h1>
            <ul>
                <li>FYP</li>
                <li>Explore</li>
                <li>Live</li>
                <li>Message</li>
            </ul>

            <button onClick={toggleTheme} className="px-2 py-2 mt-5 rounded-lg bg-[#F2F2F2] dark:bg-[#1F1F1F] dark:text-white">{theme === "dark" ? <Moon strokeWidth={2} /> : <Sun strokeWidth={2} />}</button>

            <button>Logout</button>
            <main className="relative md:ml-60 flex-1 overflow-y-auto main">
                <Outlet />
            </main>
        </div>
    );
};

export default MainLayout;