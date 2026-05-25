# UC041-046 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC041-046: Báo cáo tình hình thực hiện dự án đầu tư quý |
| **Nguồn** | UC041-046_bao-cao-tinh-hinh-thuc-hien-du-an-dt-quy_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 8 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung AC chính thức cho các luồng chính? | AC là cơ sở pass/fail cho QA. Hiện tại AC được suy luận từ workflow, cần xác nhận chính thức. | Resolved | **Đồng ý**. QA tự derive AC. BA không bổ sung thêm AC tường minh. |
| Q2 | High | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs A-002→A-010 "API, Read-only" | Trường A-002→A-010 có thực sự Read-only hay Enabled cho sửa? "Nguyên tắc trách nhiệm" nói cho phép sửa TẤT CẢ trường API-sourced, nhưng bảng UI ghi rõ Read-only. Mâu thuẫn. | Dev không biết implement Read-only hay Enabled. QA không biết expected behavior. Tương tự CMR_12 contradiction. | Resolved | **A-002→A-010 giữ Read-only**. Đã cập nhật Ngoại lệ vào UC doc. Khi API fail, A-001 giữ nguyên Dropdown để chọn, A-002→A-010 hiển thị trống và Disabled. |
| Q3 | Medium | UC041-046.1 #16-18 (strikethrough ~~) | Các trường Đơn vị tiếp nhận (#0), Quý báo cáo (#1), Năm báo cáo (#2) bị strikethrough. Chúng đã loại bỏ hoàn toàn hay chỉ ẩn? Nếu loại bỏ → Quý/Năm được xác định từ đâu (từ kỳ hạn trên listing)? | Ảnh hưởng đến test flow: nếu Quý/Năm auto-determined từ kỳ listing → V17 check trùng kỳ hoạt động khác. Cần xác nhận logic xác định kỳ. | Resolved | Đã loại bỏ **Đơn vị tiếp nhận**. **Quý/Năm** hiển thị trên UI nhưng **Disabled/Read-only**, tự động lấy từ kỳ hạn trên listing. Đã bỏ logic V17 check trên form vì hệ thống đã validate ngay khi chọn "Lập BC" ở listing (theo CF_01 Phạm vi). User muốn đổi kỳ → quay về màn hình danh sách. Qua kỳ hạn → ẩn nút Lập/Import, nhưng bản ghi cũ vẫn Sửa/Nộp được (theo CMR_03). |
| Q4 | Medium | UC041-046.2 Mục 3 — Toast messages | UC không ghi rõ text Toast Success cho Lưu nháp và Nộp. Chỉ có Toast Error cho V17. Exact text Toast Success là gì? | QA cần exact message để verify. | Resolved | **Sử dụng Toast chuẩn từ CF_01**. Không cần ghi lại riêng trong UC. |
| Q5 | Medium | UC041-046.3 #2 Import — "chưa có hồ sơ hoặc hồ sơ ở trạng thái Lưu nháp / YCCS" | Import khi đã có hồ sơ Lưu nháp: ghi đè dữ liệu hiện tại hay tạo bản ghi mới? Hành vi cụ thể khi Import vào form đã có data? | Ảnh hưởng đến data consistency. Cần xác nhận hành vi Import overwrite vs append. | Resolved | **Import ghi đè** dữ liệu hiện tại. Hệ thống hiển thị popup cảnh báo ghi đè. Cập nhật vào UC doc. Chú ý: Qua kỳ hạn thì nút [Import] ẩn, nhưng nút [Nộp] vẫn thao tác được. |
| Q6 | Medium | UC041-046.2 — NĐT blocks "Không cho phép thêm/xóa thủ công" | Khi dự án có nhiều NĐT, nếu API trả về NĐT mới (thêm sau khi BC đã Lưu nháp), BC đã lưu có tự cập nhật NĐT blocks không? Hay chỉ lấy snapshot tại thời điểm chọn dự án? | Ảnh hưởng đến data freshness và test scenario khi NĐT thay đổi giữa các lần edit. | Resolved | **Snapshot** tại thời điểm Lưu nháp. Khi **Chỉnh sửa** → **re-fetch** API để cập nhật NĐT mới. Nếu NĐT bị xóa → popup cảnh báo mất dữ liệu. Đã cập nhật vào UC doc. |
| Q7 | Low | UC041-046.2 — Decimal precision "auto-round half-up khi blur" | Khi auto-round, hệ thống có hiển thị indicator/thông báo cho người dùng biết giá trị đã bị làm tròn không? | UX concern: người dùng có thể không nhận ra giá trị đã thay đổi sau blur. | Resolved | **Đồng ý**. Không hiển thị indicator. Auto-round im lặng (áp dụng toàn hệ thống). |
| Q8 | Low | UC041-046.2 — RULE-01 "Triệu VNĐ" | Khi đơn vị là "Triệu VNĐ", decimal precision có thay đổi không? (VD: 1.5 triệu VNĐ = 1,500,000 VNĐ — cần bao nhiêu decimal?) | Ảnh hưởng đến validation rules và test data cho dự án ĐTTN. | Resolved | **Đồng ý**. Decimal precision giữ nguyên 5 chữ số cho cả USD và Triệu VNĐ. Không thay đổi. |
| Q9 | Medium | UI Design vs UC doc (Phần Header, Placeholder) | UI design hiển thị Breadcrumb và Title trang, đồng thời các trường Địa chỉ liên hệ, SĐT, Email có text placeholder cụ thể (VD: "Nhập địa chỉ liên hệ"). Các thành phần này đang thiếu trong bảng mô tả Section 4.2 của UC doc. Cần bổ sung vào tài liệu? | Thiếu sót element trong tài liệu khiến dev có thể bỏ sót placeholder và title. Cần sự thống nhất. | Resolved | **Giữ nguyên**. Không bổ sung placeholder cho A-011, A-012, A-013. |
| Q10 | High | UI Design vs UC doc (VI. Năng lượng) | UC mô tả 4 dòng cố định (Điện, Than, Dầu, Khí LNG) và nút [+ Thêm] Năng lượng khác. UI lại có icon Trash Bin ở cả 4 dòng cố định, ngụ ý cho phép xóa. Người dùng có được phép xóa 4 dòng cố định này không? Tên nút trong UI là "+ Thêm loại năng lượng", khác với UC. | Hành vi xóa các chỉ tiêu mặc định ảnh hưởng lớn đến form logic. Cần chốt lại UI hay UC đúng. | Resolved | **Xóa tính năng Thêm/Xóa**. Dòng 5 "Năng lượng khác" trở thành dòng nhập cố định. Đã cập nhật UC v1.7. |
| Q11 | High | UI Design vs UC doc (VII. Thuế) | UI có group header "VII. THUẾ" và 3 sub-rows (Thuế GTGT, Thuế TNDN, Thuế khác). UC chỉ có 1 row duy nhất "Thuế và các khoản nộp NSNN". Cái nào là chính xác? | Data structure khác nhau hoàn toàn (3 cột nhập vs 1 cột nhập). Ảnh hưởng trực tiếp cấu trúc DB và UI. | Resolved | **Dùng 1 dòng duy nhất** theo UC. UI đã xóa các dòng con. |
| Q12 | High | UI Design vs UC doc (VIII. Diện tích đất) | UI có group header "VIII. DIỆN TÍCH ĐẤT" và 2 sub-rows (Đã sử dụng, Đã thuê). UC chỉ có 1 row duy nhất "Diện tích đất, mặt nước sử dụng". Cái nào là chính xác? | Data structure khác biệt hoàn toàn (2 dòng vs 1 dòng). | Resolved | **Dùng 1 dòng duy nhất** theo UC. UI đã xóa các dòng con. |
| Q13 | Low | UI Design Typo | Dưới mục 1.2 Nhà đầu tư nước ngoài, label đang ghi là "[Nhà đầu tư Việt Nam]" thay vì "[Nhà đầu tư nước ngoài]". | Lỗi copy-paste trên file thiết kế, cần báo Designer fix. | Resolved | **Đã cập nhật** trên thiết kế. |
| Q14 | Low | UI Design vs UC doc (Table Headers) | UI Design có 3 cột dữ liệu rõ ràng (Số liệu trong kỳ, Lũy kế từ đầu năm, Lũy kế từ khi cấp GCNĐKĐT). UC doc chỉ ghi "3 cột Editable (A)(B)(C)". Cần liệt kê chính xác header 3 cột này vào Section 4 của UC doc không? | Tăng tính rõ ràng cho bảng Inventory. | Resolved | **Đã khớp**. Tên cột trong UC (dòng 123) đã đồng bộ với thiết kế. |

---

## Thống kê

| Priority | Số lượng |
|---|---|
| High | 5 |
| Medium | 5 |
| Low | 4 |
| **Tổng** | **14** |
