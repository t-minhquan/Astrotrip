from flask import Flask, render_template

app = Flask(__name__)

# --- DỮ LIỆU TOUR MÔ PHỎNG (Giống Vietravel / Saigontourist) ---
danh_sach_tours = [
    {
        "id": 1,
        "ten": "Vịnh Hạ Long - Tuyệt Tác Thiên Nhiên",
        "mo_ta": "Trải nghiệm du thuyền 5 sao, chèo kayak và khám phá các hang động kỳ vĩ giữa kỳ quan thế giới.",
        "gia": "2.500.000đ",
        "anh": "https://cafefcdn.com/203337114487263232/2023/11/8/ha-long-sss-1699415786898-1699415787023421751026-1699424995580-16994249957491431048714.jpg",
        "thoi_gian": "3 Ngày 2 Đêm",
        "phuong_tien": "Ô tô, Du thuyền",
        "lich_trinh": [
            {"ngay": "Ngày 1: Hà Nội - Vịnh Hạ Long", "noi_dung": "Xe đón quý khách tại điểm hẹn. Trưa đến bến cảng, nhận phòng du thuyền 5 sao. Chiều chèo Kayak tại khu vực hang Luồn và tự do tắm biển."},
            {"ngay": "Ngày 2: Khám phá Hang Sửng Sốt - Đảo Ti Tốp", "noi_dung": "Đón bình minh với bài tập Thái Cực Quyền. Thăm quan Hang Sửng Sốt - hang động lớn và đẹp nhất Vịnh. Trưa tham gia lớp học nấu ăn trên boong tàu."},
            {"ngay": "Ngày 3: Hạ Long - Hà Nội", "noi_dung": "Tham quan làng chài ngọc trai. Dùng bữa trưa sớm trước khi cập bến. Xe đưa quý khách về lại điểm đón ban đầu."}
        ],
        "bao_gom": ["Xe du lịch đời mới", "Du thuyền tiêu chuẩn 5 sao", "Vé tham quan các điểm", "Hướng dẫn viên nhiệt tình", "Các bữa ăn theo lịch trình"],
        "khong_bao_gom": ["Thuế VAT", "Chi phí cá nhân (điện thoại, giặt ủi)", "Tiền tip cho HDV và tài xế"]
    },
    {
        "id": 2,
        "ten": "Sapa - Chạm Tay Vào Mây Trời",
        "mo_ta": "Chinh phục nóc nhà Đông Dương Fansipan, thăm bản Cát Cát và thưởng thức đặc sản Tây Bắc.",
        "gia": "3.100.000đ",
        "anh": "https://static.vinwonders.com/production/du-lich-sa-pa-banner-1.jpg",
        "thoi_gian": "3 Ngày 2 Đêm",
        "phuong_tien": "Xe giường nằm cao cấp",
        "lich_trinh": [
            {"ngay": "Ngày 1: Khởi hành đi Sapa - Bản Cát Cát", "noi_dung": "Đến Sapa nhận phòng khách sạn. Chiều đi bộ tham quan Bản Cát Cát của người H'Mông, tìm hiểu nghề nhuộm chàm và dệt vải."},
            {"ngay": "Ngày 2: Chinh phục đỉnh Fansipan", "noi_dung": "Di chuyển bằng cáp treo lên đỉnh Fansipan - Nóc nhà Đông Dương ở độ cao 3.143m. Check-in cột mốc. Tối tự do dạo phố, thưởng thức đồ nướng."},
            {"ngay": "Ngày 3: Núi Hàm Rồng - Trở về", "noi_dung": "Tham quan KDL Núi Hàm Rồng, vườn lan Đông Dương, cổng trời. Mua sắm đặc sản chợ Sapa và lên xe trở về."}
        ],
        "bao_gom": ["Xe giường nằm khứ hồi", "Khách sạn 3 sao trung tâm", "Vé cáp treo Fansipan (Khứ hồi)", "Vé tham quan Bản Cát Cát"],
        "khong_bao_gom": ["Chi phí ăn uống ngoài chương trình", "Vé tàu hỏa leo núi Mường Hoa"]
    },
    {
        "id": 3,
        "ten": "Khám Phá Rừng Nam Cát Tiên",
        "mo_ta": "Hành trình trekking hòa mình vào thiên nhiên hoang dã và trải nghiệm ngắm thú đêm kỳ thú.",
        "gia": "1.450.000đ",
        "anh": "https://media.hangthat.vn/uploads/2025/10/12/dnt-nct-lake1-1760282638.jpg",
        "thoi_gian": "2 Ngày 1 Đêm",
        "phuong_tien": "Xe ghế ngồi",
        "lich_trinh": [
            {"ngay": "Ngày 1: Tp.HCM - Rừng Nam Cát Tiên", "noi_dung": "Di chuyển đến VQG Nam Cát Tiên. Chiều trekking xuyên rừng khám phá hệ sinh thái đa dạng, thăm Cây Tung trăm tuổi. Tối trải nghiệm đi xe đặc chủng ngắm thú đêm đi kiếm ăn."},
            {"ngay": "Ngày 2: Bàu Sấu - Tp.HCM", "noi_dung": "Đạp xe và đi bộ xuyên rừng vào Bàu Sấu - khu đất ngập nước tuyệt đẹp. Khám phá môi trường sống của cá sấu nước ngọt. Chiều lên xe trở về Tp.HCM."}
        ],
        "bao_gom": ["Xe đưa đón khứ hồi", "Vé vào cổng VQG", "Xe đặc chủng ngắm thú đêm", "Hướng dẫn viên bản địa", "Bảo hiểm du lịch"],
        "khong_bao_gom": ["Phí thuê xe đạp", "Chi phí cá nhân phát sinh"]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tours')
def tours():
    return render_template('tours.html', tours=danh_sach_tours)

# Route mới: Khi bấm vào 1 tour, nó sẽ tìm id tương ứng và mở trang chi tiết
@app.route('/tour/<int:tour_id>')
def tour_detail(tour_id):
    # Tìm tour có id khớp với id được truyền vào
    tour = next((t for t in danh_sach_tours if t["id"] == tour_id), None)
    if tour:
        return render_template('tour_detail.html', tour=tour)
    return "Không tìm thấy Tour này!", 404

if __name__ == '__main__':
    app.run(debug=True)